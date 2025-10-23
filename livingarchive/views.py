# livingarchive/views.py
import json
import logging
from typing import Dict, Any, List

from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseNotAllowed, HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.exceptions import ValidationError

from .models import CesiumPin
from .utils import validate_coordinates

logger = logging.getLogger(__name__)

def cesium_view(request: HttpRequest) -> HttpResponse:
    """Render the 3D visualization page"""
    context: Dict[str, Any] = {
        'GOOGLE_MAPS_API_KEY': settings.WAGTAIL_ADDRESS_MAP_KEY,
    }
    return render(request, "cesium/tileset_annotations.html", context)

# ---- DB-backed API ----
def annotations_geojson(request: HttpRequest) -> JsonResponse:
    """Get all annotations in GeoJSON format"""
    features: List[Dict[str, Any]] = [p.as_feature() for p in CesiumPin.objects.order_by("pk")]
    return JsonResponse({
        "type": "FeatureCollection", 
        "features": features
    })

@csrf_exempt
@login_required
def annotations_create(request: HttpRequest) -> HttpResponse:
    """Create a new annotation (requires login)"""
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    
    try:
        data: Dict[str, Any] = json.loads(request.body.decode("utf-8"))
        
        # Basic validation
        required_fields: List[str] = ['lon', 'lat']
        if not all(field in data for field in required_fields):
            return HttpResponseBadRequest(
                json.dumps({"ok": False, "error": "Missing required fields"}),
                content_type="application/json"
            )
        
        # Create the pin with the current user
        p: CesiumPin = CesiumPin.objects.create(
            title=data.get("title", "").strip()[:200],
            notes=data.get("notes", ""),
            lon=float(data["lon"]),
            lat=float(data["lat"]),
            height=float(data.get("height") or 0),
            created_by=request.user
        )
        return JsonResponse({"ok": True, "id": p.pk})
        
    except ValueError as e:
        return HttpResponseBadRequest(
            json.dumps({"ok": False, "error": "Invalid coordinates"}),
            content_type="application/json"
        )
    except Exception as e:
        return HttpResponseBadRequest(
            json.dumps({"ok": False, "error": str(e)}),
            content_type="application/json"
        )

@csrf_exempt
def annotations_update_delete(request, pk):
    try:
        p = CesiumPin.objects.get(pk=pk)
    except CesiumPin.DoesNotExist:
        return HttpResponseBadRequest(
            json.dumps({"ok": False, "error": "not found"}),
            content_type="application/json"
        )

    if request.method == "DELETE":
        p.delete()
        return JsonResponse({"ok": True})

    if request.method == "PATCH":
        data = json.loads(request.body.decode("utf-8"))
        if "title" in data:  p.title  = data["title"].strip()[:200]
        if "notes" in data:  p.notes  = data["notes"]
        if "lon"   in data:  p.lon    = float(data["lon"])
        if "lat"   in data:  p.lat    = float(data["lat"])
        if "height" in data: p.height = float(data["height"])
        p.save()
        return JsonResponse({"ok": True})

    return HttpResponseNotAllowed(["DELETE", "PATCH"])
