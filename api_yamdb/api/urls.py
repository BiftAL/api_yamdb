from django.urls import include, path


urlpatterns = [
    path('v1/titles/', include('reviews_comments.urls')),
]
