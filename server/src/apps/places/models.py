from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

class Memory(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Владелец',
        related_name='memories',
    )

    name  = models.CharField(
        max_length=55,
        verbose_name='Название места',
    )

    comment = models. TextField(
        max_length=55,
        verbose_name='Комментарий',
    )

    latitude = models.DecimalField(
        verbose_name='Широта',
        max_digits=10,
        decimal_places=5,
        default=0.0
    )
    longitude = models.DecimalField(
        verbose_name='Долгота',
        max_digits=10,
        decimal_places=5,
        default=0.0
    )

    def get_image_url(self):
        return f"https://maps.geoapify.com/v1/staticmap?style=osm-carto&center=lonlat:{self.longitude},{self.latitude}&zoom=16&marker=lonlat:{self.longitude},{self.latitude};color:%23ff0000;size:medium&apiKey={settings.GEOAPIFY_STATIC_MAPS_API_KEY}"

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Воспоминание'
        verbose_name_plural = 'Воспоминания'
        ordering = ['-id']
