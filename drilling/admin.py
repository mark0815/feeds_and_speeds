from django.contrib import admin
from .models import (
    Drill,
)


@admin.register(Drill)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ("flute_count", "diameter", "material", "drill_type")
    list_filter = ("material", "drill_type")