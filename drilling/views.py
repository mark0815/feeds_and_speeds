from .models import Drill
from rest_framework import viewsets
from .serializers import (
    DrillSerializer,
)


class DrillViewSet(viewsets.ModelViewSet):
    queryset = Drill.objects.all()
    serializer_class = DrillSerializer
