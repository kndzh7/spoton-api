from django.db import models


class Order(models.Model):
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    STATUSES = [
        ('new', 'Новый'),
        ('accepted', 'Принят'),
        ('canceled', 'Отменен'),
    ]

    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата последнего изменения', auto_now=True)
    performer = models.ForeignKey('user.Performer', models.SET_NULL, related_name='performers', blank=True, null=True)
    status = models.CharField('Статус', choices=STATUSES, max_length=8, default='new')

    def __str__(self):
        return f'Заказ #{self.id} | {self.get_status_display()}'
