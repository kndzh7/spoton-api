from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from .models import Performer
from .serializers import PerformerSerializer


class PerformerViewSet(mixins.CreateModelMixin,
                       GenericViewSet):
    serializer_class = PerformerSerializer
    swagger_tags = ["performers"]
    queryset = Performer.objects.all()
