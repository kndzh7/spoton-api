import datetime

from celery import shared_task
from django.utils import timezone

from .models import Order


@shared_task
def order_checker():
    five_minutes_ago = timezone.now() + datetime.timedelta(minutes=-5)
    orders = Order.objects.filter(created_at__lte=five_minutes_ago, status='new').update(status='canceled')
