from .models import Material, MaterialClass
from rest_framework import viewsets
from .serializers import (
    MaterialClassSerializer,
    MaterialSerializer,
)


class MaterialClassViewSet(viewsets.ModelViewSet):
    queryset = MaterialClass.objects.all()
    serializer_class = MaterialClassSerializer


class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
