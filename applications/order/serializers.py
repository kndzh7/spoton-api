from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from .exceptions import OrderBadStatusException, OrderDoesNotExistException
from .models import Order
from applications.user.serializers import PerformerSerializer
from applications.user.models import Performer
from ..user.exceptions import PerformerDoesNotExistException


class OrderSerializer(serializers.ModelSerializer):
    status = serializers.CharField(read_only=True)
    performer = serializers.IntegerField(read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'status', 'created_at', 'updated_at', 'performer')


class OrderAssignSerializer(serializers.Serializer):
    order = serializers.IntegerField(required=True)
    performer = serializers.IntegerField(required=True)

    class Meta:
        model = Order
        fields = ('order', 'performer')

    @staticmethod
    def get_order(order: int) -> Order:
        if not Order.objects.filter(id=order).exists():
            raise OrderDoesNotExistException
        return Order.objects.get(id=order)

    @staticmethod
    def get_performer(performer: int) -> Performer:
        if not Performer.objects.filter(id=performer).exists():
            raise PerformerDoesNotExistException
        return Performer.objects.get(id=performer)

    def save(self, **kwargs):
        order = self.get_order(self.data['order'])
        performer = self.get_performer(self.data['performer'])

        if order.status != 'new':
            raise OrderBadStatusException

        order.performer = performer
        order.status = 'accepted'
        order.save()
        return order


class OrderAssignResponseSerializer(serializers.ModelSerializer):
    performer = PerformerSerializer()

    class Meta:
        fields = ('performer', )
        model = Order
