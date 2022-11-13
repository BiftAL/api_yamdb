import random

from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import AccessToken

from .models import User
from .serializers import (TokenSerializer, UserAdminCreateSerializer,
                          UserFieldsSerializer, UserSignUpSerializer)

from api_yamdb.settings import EMAIL_HOST_USER
from api.permissions import IsAuthenticatedAdmin


class UserRUDView(APIView):
    """Вью для операций с пользователем. (получение, обновление, удаление)"""
    permission_classes = [IsAuthenticatedAdmin]

    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        serializer = UserFieldsSerializer(user)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def patch(self, request, username):
        user = get_object_or_404(User, username=username)
        serializer = UserFieldsSerializer(
            user,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.validated_data,
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, username):
        user = get_object_or_404(User, username=username)
        if user:
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class UsersViewSet(viewsets.ModelViewSet):
    """Вью для создания пользователей администратором."""
    queryset = User.objects.all()
    serializer_class = UserAdminCreateSerializer
    permission_classes = (permissions.IsAuthenticated, IsAuthenticatedAdmin)
    pagination_class = PageNumberPagination

    def has_permission(self, request, view):
        return self.get_permissions()

    def get_current_path(self, request):
        return {
            'current_path': request.get_full_path()
        }

    def get_permissions(self):
        if self.get_current_path(self.request) == '/api/v1/users/me/':
            return (permissions.IsAuthenticated(),)
        return (IsAuthenticatedAdmin(),)

    @action(
        detail=False,
        methods=['GET', 'PATCH'],
        permission_classes=(permissions.IsAuthenticated,),
        url_path='me'
    )
    def me(self, request):
        # print(request.path)
        user = User.objects.get(id=request.user.pk)
        # print(self.get_current_path(self, request))
        if request.method == 'GET':
            serializer = UserFieldsSerializer(user)
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        elif request.method == 'PATCH':
            new_query_dict = self.request.data.copy()
            if not request.user.is_admin and not request.user.is_superuser:
                new_query_dict['role'] = request.user.role
            serializer = UserFieldsSerializer(
                user,
                data=new_query_dict,
                partial=True
            )
            if serializer.is_valid():
                serializer.save()
                return Response(
                    serializer.validated_data,
                    status=status.HTTP_200_OK
                )
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )


class CreateUserView(APIView):
    """Вью для самостоятельной регистрации пользователя."""
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
                EMAIL_HOST_USER,
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
    """Вью для получения токена."""
    def post(self, request):
        serializer = TokenSerializer(data=request.data)
        if serializer.is_valid():
            fields = serializer.validated_data
            user = get_object_or_404(User, username=fields['username'])
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
