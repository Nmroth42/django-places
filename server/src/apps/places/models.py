from django.contrib.auth.models import User
from django.db import models


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

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Воспоминание'
        verbose_name_plural = 'Воспоминания'
        ordering = ['-id']
