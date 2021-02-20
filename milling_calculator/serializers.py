from rest_framework import serializers
from .models import CuttingData, Machine, Vendor, Tool


class CuttingDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CuttingData
        fields = ["id", "tool", "material", "fz", "vc"]


class MachineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Machine
        fields = ["id", "name", "spindle_net_power_kw", "max_rpm", "max_cutting_speed"]


class VendorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vendor
        fields = ["id", "name"]


class ToolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tool
        fields = ["id", "vendor", "name", "flute_count", "diameter", "flute_length"]
