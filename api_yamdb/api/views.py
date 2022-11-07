import random

from django.core.mail import send_mail
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import AccessToken

from users.models import User
from .serializers import TokenSerializer, UserSerializer


class CreateUserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            code = random.randint(1000, 9999)
            user = serializer.save(confirmation_code=code)
            send_mail(
                'YAMDB API confirmation code',
                str(code),
                'fromAPI@yamdb.com',
                [user.email],
                fail_silently=False,
            )
            return Response(
                {'email': user.email, 'username': user.username},
                status=status.HTTP_200_OK
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class GetAPIToken(APIView):
    def post(self, request):
        serializer = TokenSerializer(data=request.data)
        if serializer.is_valid():
            fields = serializer.validated_data
            try:
                user = User.objects.get(username=fields['username'])
            except User.DoesNotExist:
                return Response(
                    {'Несуществующий юзер'},
                    status=status.HTTP_404_NOT_FOUND
                )
            if fields['confirmation_code'] == user.confirmation_code:
                token = AccessToken.for_user(user)
                return Response(
                    {'token': str(token)},
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {'Неверный код'},
                    status=status.HTTP_400_BAD_REQUEST
                )
        return Response(
            {'Неверные данные'},
            status=status.HTTP_400_BAD_REQUEST
        )
