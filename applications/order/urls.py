from rest_framework.routers import DefaultRouter
from .views import OrderViewSet

order_router = DefaultRouter()
order_router.register('order', OrderViewSet, basename='order')
