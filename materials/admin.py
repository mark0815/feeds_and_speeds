from machinist_toolbox.admin_helper import changelist_link
from django.contrib import admin
from .models import (
    MaterialClass,
    Material,
)


@admin.register(MaterialClass)
class MaterialClassAdmin(admin.ModelAdmin):
    list_display = ("name", "list_materials_count")

    def list_materials_count(self, obj: MaterialClass) -> str:
        return changelist_link(
            Material,
            f"{obj.materials.count()} Materials",
            {"material_class__id__exact": f"{obj.id}"},
        )

    list_materials_count.short_description = "Materials"


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ("material_class", "name", "kc_1_1", "mc")
    list_filter = ["material_class"]
