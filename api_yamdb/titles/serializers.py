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
        sum_of_scores = 0
        count_of_scores = 0

        for i in obj.reviews.filter(title_id=obj.pk):
            sum_of_scores += i.score
            count_of_scores += 1

        return int(sum_of_scores / count_of_scores)
