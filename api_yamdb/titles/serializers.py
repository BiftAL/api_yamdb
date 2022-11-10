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
    category = serializers.SlugRelatedField(slug_field='slug', queryset=models.Category.objects)
    genre = serializers.SlugRelatedField(many=True, slug_field='slug', queryset=models.Genre.objects)

    class Meta:
        fields = (
            'id', 'name', 'year', 'rating', 'description', 'genre', 'category'
        )
        model = models.Title

    def create(self, validated_data):
        genres = validated_data.pop('genre')
        title = models.Title.objects.create(**validated_data)
        for genre in genres:
            models.GenreTitle.objects.create(genre=genre, title=title)
        return title

        #def to_representation(self, instance):

    def to_representation(self, instance):
        # print(self.data)
        data = TitleSerializer.to_representation(instance)
        return data

    def get_rating(self, obj):
        sum_of_scores = 0
        count_of_scores = 0
        count = None

        for i in obj.reviews.filter(title_id=obj.pk):
            sum_of_scores += i.score
            count_of_scores += 1

        if count_of_scores > 0:
            count = int(sum_of_scores / count_of_scores)

        return count
