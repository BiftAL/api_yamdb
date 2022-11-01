from django.contrib import admin

from .models import Category, Genre, Title


class CategoryAdmin(admin.ModelAdmin):
    """модель категории произведения"""
    list_display = ('pk', 'name', 'slug')


class GenreAdmin(admin.ModelAdmin):
    """модель жанра произведения"""
    list_display = ('pk', 'name', 'slug')


class TitleAdmin(admin.ModelAdmin):
    """модель произведения"""
    list_display = ('pk', 'name', 'year', 'description', 'category')
    filter_horizontal = ('genre',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Title, TitleAdmin)
