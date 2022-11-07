from django.urls import include, path, re_path
from .views import CreateUserView, GetAPIToken, GetAPIUsers
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    path('v1/titles/', include('reviews_comments.urls')),
    path('v1/auth/signup/', CreateUserView.as_view(), name='signup'),
    path('v1/auth/token/', GetAPIToken.as_view(), name='token'),
    re_path(r'^v1/titles/(?P<title_id>[\d]+)/reviews/', include('reviews_comments.urls')),
    path('v1/users/', include(router.urls)),
]
