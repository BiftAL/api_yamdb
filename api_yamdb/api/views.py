import random

from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework import permissions, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.pagination import PageNumberPagination

from users.models import User
from .serializers import (TokenSerializer, UserFieldsSerializer,
                          UserSignUpSerializer, UserAdminCreateSerializer)


class UserRUDView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        return Response(
            user,
            status=status.HTTP_200_OK
        )


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserAdminCreateSerializer
    pagination_class = PageNumberPagination

    def perform_create(self, serializer):
        if self.request.data.get('role') is None:
            self.request.POST._mutable = True
            self.request.data['role'] = "user"
            self.request.POST._mutable = False
        serializer.save(role=self.request.data['role'])


class CreateUserView(APIView):
    def post(self, request):
        serializer = UserSignUpSerializer(data=request.data)
        if serializer.is_valid():
            code = random.randint(1000, 9999)
            user = serializer.save(
                confirmation_code=code,
            )
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


class GetUserInfoView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = User.objects.get(id=request.user.pk)
        serializer = UserFieldsSerializer(user)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def patch(self, request):
        user = User.objects.get(id=request.user.pk)
        serializer = UserFieldsSerializer(
            user,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.validated_data,
                status=status.HTTP_204_NO_CONTENT
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
