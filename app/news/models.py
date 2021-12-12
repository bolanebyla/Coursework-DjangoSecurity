from django.db import models


class News(models.Model):
    title = models.CharField('Название', max_length=150)
    text = models.TextField('Новость')

    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-creation_date']
