from django.urls import include, path
from rest_framework import routers
from titles import views

router = routers.DefaultRouter()
router.register(r'categories', views.CategoryViewSet)

urlpatterns = [
    path('', include(router.urls))
]
