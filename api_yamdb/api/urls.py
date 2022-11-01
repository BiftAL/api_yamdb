from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path('v1/titles/', include('reviews_comments.urls')),
    path(
        'auth/token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
]
