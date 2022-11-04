from django.urls import include, path
from rest_framework import routers
from titles import views

router = routers.DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'genres', views.GenreViewSet)

urlpatterns = [
    path('', include(router.urls))
]
