from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import Order
from .serializers import OrderSerializer, OrderAssignSerializer, OrderAssignResponseSerializer


class OrderViewSet(mixins.CreateModelMixin,
                   GenericViewSet):
    serializer_class = OrderSerializer
    swagger_tags = ["orders"]
    queryset = Order.objects.all()

    @swagger_auto_schema(method='post',
                         request_body=OrderAssignSerializer,
                         responses={200: OrderAssignResponseSerializer})
    @action(detail=False, methods=['post'])
    def assign(self, request):
        serializer = OrderAssignSerializer(data=request.data, context=self.get_serializer_context())
        serializer.is_valid(raise_exception=True)
        order = serializer.save()
        response = OrderAssignResponseSerializer(instance=order).data
        return Response(data=response)
