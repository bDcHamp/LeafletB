from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from typing import Dict, Any, Optional, Union
from datetime import datetime
from .utils import validate_coordinates, format_location_str

class CesiumPin(models.Model):
    """Model for storing pins/markers on the Cesium map"""
    
    title = models.CharField(_('Title'), max_length=200)
    notes = models.TextField(_('Notes'), blank=True)
    lon = models.FloatField(_('Longitude'))
    lat = models.FloatField(_('Latitude'))
    height = models.FloatField(_('Height'), default=0)
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated At'), auto_now=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='created_pins',
        verbose_name=_('Created By')
    )

    class Meta:
        verbose_name = _('Cesium Pin')
        verbose_name_plural = _('Cesium Pins')
        ordering = ['-created_at']

    def __str__(self) -> str:
        return f"{self.title} ({self.lat}, {self.lon})"

    def as_feature(self) -> Dict[str, Any]:
        """Convert the pin to GeoJSON feature format"""
        return {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [self.lon, self.lat, self.height]
            },
            "properties": {
                "id": self.pk,  # Use pk instead of id for better type checking
                "title": self.title,
                "notes": self.notes,
                "height": self.height,
                "created_at": self.created_at.isoformat(),
                "created_by": self.created_by.username if self.created_by else None,
            },
        }

    def clean(self) -> None:
        """Validate the model data"""
        super().clean()
        if not -90 <= self.lat <= 90:
            raise ValidationError({'lat': _('Latitude must be between -90 and 90')})
        if not -180 <= self.lon <= 180:
            raise ValidationError({'lon': _('Longitude must be between -180 and 180')})
