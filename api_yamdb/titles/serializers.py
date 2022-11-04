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


class TitleSerializer(serializers.ModelSerializer):
    """сериализатор произведений"""
    rating = serializers.SerializerMethodField()

    class Meta:
        fields = (
            'id', 'name', 'year', 'rating', 'description', 'genres', 'category'
        )
        model = models.Title

    def get_rating(self, obj):
        return "в работе"
