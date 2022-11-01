from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import ReviewViewSet, CommentViewSet

router = DefaultRouter()

router.register(
    r'(?P<title_id>[\d]+)/reviews',
    ReviewViewSet,
    basename='review'
)
router.register(
    r'(?P<title_id>[\d]+)/reviews/(?P<review_id>[\d]+)/comments',
    CommentViewSet,
    basename='comment'
)

urlpatterns = [
    path('', include(router.urls)),
]