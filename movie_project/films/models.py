from django.db import models

# Create your models here.
class Films_Post(models.Model):
    title = models.CharField('Название фильма', max_length=100)
    description = models.TextField('Описание фильма', max_length=300)
    review = models.TextField('Отзыв на фильм')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'