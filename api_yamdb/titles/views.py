from rest_framework import filters, pagination, viewsets

from . import models, serializers


class CategoryViewSet(viewsets.ModelViewSet):
    """вьюсет категорий"""
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    pagination_class = pagination.LimitOffsetPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'
