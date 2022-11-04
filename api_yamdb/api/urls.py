from django.urls import include, path, re_path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import UserViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'signup', UserViewSet, basename='signup')

urlpatterns = [
    path('v1/titles/', include('reviews_comments.urls')),
    path('v1/auth/', include(router.urls)),
    re_path(
        r'^v1/titles/(?P<title_id>[\d]+)/reviews/',
        include('reviews_comments.urls')
    ),
    path(
        'v1/auth/token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path('v1/', include('titles.urls'))
]
