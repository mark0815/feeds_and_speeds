from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from machinist_toolbox.admin_helper import changelist_link

from .models import Material, MaterialClass


@admin.register(MaterialClass)
class MaterialClassAdmin(admin.ModelAdmin):
    list_display = ("name", "list_materials_count")

    def list_materials_count(self, obj: MaterialClass) -> str:
        return changelist_link(
            Material,
            _("%(count)s Materials") % {"count": obj.materials.count()},
            {"material_class__id__exact": f"{obj.id}"},
        )

    list_materials_count.short_description = _("Materials")  # type: ignore


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ("material_class", "name", "kc_1_1", "mc")
    list_filter = ["material_class"]
