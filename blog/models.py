from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    body = models.TextField(verbose_name='Содержимое')
    slug = models.CharField(max_length=150, verbose_name='slug', null=True, blank=True)
    preview = models.ImageField(upload_to='blog/photo', blank=True, null=True, verbose_name='Изображение')
    created_at = models.DateField(
        auto_now_add=True,
        verbose_name="Дата создания",
    )
    views_count = models.IntegerField(default=0, verbose_name="Просмотры")
    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано'
    )


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'