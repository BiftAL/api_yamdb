from django.db import models


class Title(models.Model):
    """модель произведения"""
    name = models.CharField(
        max_length=100,
        verbose_name='Название', help_text='Название произведения'
    )
    year = models.