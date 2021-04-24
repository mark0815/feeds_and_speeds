from rest_framework import viewsets

from .models import CuttingData, Machine, Tool, Vendor
from .serializers import (
    CuttingDataSerializer,
    MachineSerializer,
    ToolSerializer,
    VendorSerializer,
)


class CuttingDataViewSet(viewsets.ModelViewSet):
    queryset = CuttingData.objects.all()
    serializer_class = CuttingDataSerializer


class MachineViewSet(viewsets.ModelViewSet):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer


class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class ToolViewSet(viewsets.ModelViewSet):
    queryset = Tool.objects.all()
    serializer_class = ToolSerializer
