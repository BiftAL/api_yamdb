import random
from rest_framework import permissions, viewsets
from users.models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['post', ]

    def perform_create(self, serializer):
        code = random.randint(1000, 9999)
        user = serializer.save(confirmation_code=code)
        print(user.confirmation_code)
