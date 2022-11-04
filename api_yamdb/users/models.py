from django.db import models
from django.contrib.auth.models import AbstractUser

ROLE_CHOICES = (
    ('anon', 'Аноним '),
    ('user', 'Аутентифицированный'),
    ('moderator', 'Модератор'),
    ('admin', 'Администратор'),
    ('superuser', 'Суперюзер'),
)


class User(AbstractUser):
    bio = models.TextField(
        'Биография',
        blank=True,
    )
    role = models.TextField(
        'Роль',
        blank=True,
        max_length=16,
        choices=ROLE_CHOICES,
    )
    confirmation_code = models.IntegerField(
        'Код подтверждения',
        null=True,
    )
