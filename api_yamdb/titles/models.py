from django.db import models


class Category(models.Model):
    """модель категории"""
    pass


class Title(models.Model):
    """модель произведения"""
    name = models.CharField(
        max_length=100,
        verbose_name='Название', help_text='Название произведения'
    )
    year = models.IntegerField(
        max_length=4, verbose_name='Год', help_text='Год выхода'
    )
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, related_name='titles',
        verbose_name='Категория', help_text='Категория произведения'
    )
