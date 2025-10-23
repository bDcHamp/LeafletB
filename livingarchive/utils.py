from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_coordinates(lat, lon):
    """Validate latitude and longitude coordinates"""
    if not -90 <= lat <= 90:
        raise ValidationError({'lat': _('Latitude must be between -90 and 90')})
    if not -180 <= lon <= 180:
        raise ValidationError({'lon': _('Longitude must be between -180 and 180')})

def format_location_str(lat, lon):
    """Format location coordinates as a string"""
    return f"({lat:.6f}, {lon:.6f})"