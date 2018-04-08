from django.db import models
from django import forms


class Subscriber(models.Model):
    email = models.EmailField()

    def __str__(self):
        return "Пользователь %s" % (self.email)

    class Meta:
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'

