from django.db import models


class Performer(models.Model):
    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'

    username = models.CharField('Логин', max_length=25, unique=True)
    phone = models.CharField('Номер телефона', max_length=10)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    def __str__(self):
        return self.username
