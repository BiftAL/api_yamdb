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
    category = CategorySerializer(read_only=True)
    genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        fields = (
            'id', 'name', 'year', 'rating', 'description', 'genres', 'category'
        )
        model = models.Title

    #def create(self, data):
    #    """Проверка на уникальность обзора к произведению."""
    #    if Review.objects.filter(
    #            author=data.get('author'),
    #            title=data.get('title')
    #    ):
    #        raise serializers.ValidationError(
    #            'Вы уже оставляли отзыв на это произведение!'
    #        )
    #    return Review.objects.create(**data)

    def create(self, data):
        #genres = validated_data.pop('genres')
        #category = validated_data.pop('category')
        print(data)
        #title = models.Title.objects.create(**validated_data)
        # for genre in genres:
            #print(genre)
            #current_genre, status = models.Genre.objects.get(**genre)
        return models.Title.objects.create(**data)

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
