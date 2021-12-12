from django.db import models


class TestData(models.Model):
    text = models.TextField('Текст')
