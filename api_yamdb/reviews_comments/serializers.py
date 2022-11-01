from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Review, Comment


class ReviewSerializer(serializers.ModelSerializer):
    """Сериализатор для работы с отзывами."""

    # author = serializers.SlugRelatedField(
    #     read_only=True, slug_field='username'
    # )

    class Meta:
        fields = ('id', 'text', 'author', 'score', 'pub_date')
        read_only_fields = ('id', 'title_id')
        model = Review
        validators = [
            UniqueTogetherValidator(
                queryset=Review.objects.all(),
                fields=('user', 'title_id'),
                message='Вы уже оставляли отзыв на это произведение!'
            )
        ]


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для работы с комментариями."""

    # author = serializers.SlugRelatedField(
    #     read_only=True, slug_field='username'
    # )

    class Meta:
        fields = '__all__'
        read_only_fields = ('id', 'review_id')
        model = Comment
