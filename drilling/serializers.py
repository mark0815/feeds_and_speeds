from rest_framework import serializers
from .models import Drill


class DrillSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Drill
        fields = ["id", "name"]