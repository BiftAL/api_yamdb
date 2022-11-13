from django.urls import include, path, re_path
from rest_framework import routers

from users.views import UserRUDView, UsersViewSet

router_v1 = routers.DefaultRouter()
router_v1.register(r'users', UsersViewSet, basename='users')

urlpatterns = [
    path('v1/', include('titles.urls')),
    path('v1/auth/', include('users.urls')),
    # path('v1/users/me/', GetUserInfoView.as_view(), name='me'),
    re_path(
        r'^v1/users/(?P<username>[\w.@+-]+)/$',
        UserRUDView.as_view(),
        name='user'
    ),
    path('v1/', include(router_v1.urls)),
    re_path(
        r'^v1/titles/(?P<title_id>[\d]+)/reviews/',
        include('reviews.urls')
    ),
]
