from django.db import models


class Category(models.Model):
    """модель категории произведения"""
    name = models.CharField(
        max_length=256, verbose_name='Название', help_text='Название категории'
    )
    slug = models.SlugField(
        unique=False,
        verbose_name='Slug', help_text='Адрес категории в адресной строке'
    )

    def __str__(self):
        return self.name


class Genre(models.Model):
    """модель жанра произведения"""
    name = models.CharField(
        max_length=256, verbose_name='Название', help_text='Название жанра'
    )
    slug = models.SlugField(
        unique=False,
        verbose_name='Slug', help_text='Адрес жанра в адресной строке'
    )

    def __str__(self):
        return self.name


class Title(models.Model):
    """модель произведения"""
    name = models.CharField(
        max_length=100,
        verbose_name='Название', help_text='Название произведения'
    )
    year = models.IntegerField(
        verbose_name='Год выпуска', help_text='Год выпуска произведения'
    )
    # rating = integer (Рейтинг на основе отзывов, если отзывов нет — `None`)
    description = models.TextField(
        verbose_name='Описание', help_text='Описание произведения'
    )
    genre = models.ManyToManyField(Genre, through='GenreTitle')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, related_name='titles',
        verbose_name='Категория', help_text='Категория произведения'
    )

    def __str__(self):
        return self.name


class GenreTitle(models.Model):
    """связующая жанры с произведениями модель"""
    title = models.ForeignKey(Title, on_delete=models.SET_NULL, null=True)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
