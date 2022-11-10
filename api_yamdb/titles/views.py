from rest_framework import filters, pagination, viewsets, mixins

from . import models, serializers
from .permissions import IsAdminOrReadOnly


class CategoryViewSet(mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    """Вьюсет категорий."""

    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = pagination.LimitOffsetPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'


class GenreViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
    """Вьюсет жанров."""

    queryset = models.Genre.objects.all()
    serializer_class = serializers.GenreSerializer
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = pagination.LimitOffsetPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'


class TitleViewSet(viewsets.ModelViewSet):
    """Вьюсет произведений."""

    queryset = models.Title.objects.all()
    serializer_class = serializers.TitleSerializer
    permission_classes = [IsAdminOrReadOnly]


