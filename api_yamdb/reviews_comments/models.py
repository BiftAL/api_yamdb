from django.db import models

# from users.models import User


class Review(models.Model):
    """Здесь хранятся отзывы к произведениям."""

    title_id = models.TextField('ID произведения',)
    text = models.TextField('Текст отзыва', )
    author = models.TextField('Автор обзора',)
    # author = models.ForeignKey(
    #    User, on_delete=models.CASCADE, related_name='reviews')
    score = models.DecimalField(max_digits=2, decimal_places=0)
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Comment(models.Model):
    """Здесь хранятся комментарии к отзывам о произведениях."""

    review_id = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField('Текст комментария',)
    author = models.TextField('Автор комментария', )
    # author = models.ForeignKey(
    #    User, on_delete=models.CASCADE, related_name='comments')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
