from rest_framework import serializers
from .models import CuttingData, Machine, MaterialClass, Material, Vendor, Tool


class CuttingDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CuttingData
        fields = ["id", "tool", "material", "fz", "vc"]


class MachineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Machine
        fields = ["id", "name", "spindle_net_power_kw", "max_rpm", "max_cutting_speed"]


class MaterialClassSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MaterialClass
        fields = ["id", "name"]


class MaterialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Material
        fields = ["id", "material_class", "name", "kc_1_1", "mc"]


class VendorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vendor
        fields = ["id", "name"]


class ToolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tool
        fields = ["id", "vendor", "name", "flute_count", "diameter", "flute_length"]
