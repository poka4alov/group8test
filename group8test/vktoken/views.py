from rest_framework import viewsets
from .serializers import VkUserSerializer, VkTokenSerializer
from .models import VkUser


class VkUserViewSet(viewsets.ModelViewSet):
    queryset = VkUser.objects.all()
    serializer_class = VkUserSerializer


class VkTokenViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = VkUser.objects.all()
    serializer_class = VkTokenSerializer

