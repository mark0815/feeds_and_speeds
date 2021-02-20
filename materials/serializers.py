from rest_framework import serializers
from .models import MaterialClass, Material


class MaterialClassSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MaterialClass
        fields = ["id", "name"]


class MaterialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Material
        fields = ["id", "material_class", "name", "kc_1_1", "mc"]
