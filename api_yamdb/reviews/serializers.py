from rest_framework import serializers

from .models import Review, Comment


class ReviewSerializer(serializers.ModelSerializer):
    """Сериализатор для работы с отзывами."""

    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault()
    )

    def create(self, data):
        """Проверка на уникальность обзора к произведению."""
        if Review.objects.filter(
                author=data.get('author'),
                title=data.get('title')
        ):
            raise serializers.ValidationError(
                'Вы уже оставляли отзыв на это произведение!'
            )
        return Review.objects.create(**data)

    class Meta:
        fields = ('id', 'text', 'author', 'score', 'pub_date')
        read_only_fields = ('id',)
        model = Review


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для работы с комментариями."""

    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        read_only_fields = ('id', 'review_id')
        model = Comment
