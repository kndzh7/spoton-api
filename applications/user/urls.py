from rest_framework.routers import DefaultRouter
from .views import PerformerViewSet

user_router = DefaultRouter()
user_router.register('performer_create', PerformerViewSet, basename='performers')
