from rest_framework import serializers

from . import models


class CategorySerializer(serializers.ModelSerializer):
    """сериализатор категорий"""
    class Meta:
        fields = ('name', 'slug')
        model = models.Category
        lookup_field = 'slug'


class GenreSerializer(serializers.ModelSerializer):
    """сериализатор жанров"""
    class Meta:
        fields = ('name', 'slug')
        model = models.Genre
        lookup_field = 'slug'
