from django.urls import include, path, re_path
from rest_framework import routers

from .views import CreateUserView, GetAPIToken, GetUserInfoView, UsersView

router = routers.DefaultRouter()

urlpatterns = [
    path('v1/', include('titles.urls')),
    path('v1/auth/signup/', CreateUserView.as_view(), name='signup'),
    path('v1/auth/token/', GetAPIToken.as_view(), name='token'),
    path('v1/users/', UsersView.as_view(), name='users'),
    path('v1/users/me/', GetUserInfoView.as_view(), name='me'),
    re_path(
        r'^v1/titles/(?P<title_id>[\d]+)/reviews/',
        include('reviews.urls')
    ),
]
