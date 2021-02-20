from .models import CuttingData, Machine, Vendor, Tool
from rest_framework import viewsets
from .serializers import (
    CuttingDataSerializer,
    MachineSerializer,
    VendorSerializer,
    ToolSerializer,
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
