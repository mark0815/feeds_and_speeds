from machinist_toolbox.admin_helper import changelist_link
from django.contrib import admin
from .models import (
    CuttingData,
    CuttingRecipe,
    Machine,
    Vendor,
    Tool,
)


@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    list_display = ("name", "spindle_net_power_kw", "max_rpm", "max_vf")


@admin.register(Vendor)
class ToolVendorAdmin(admin.ModelAdmin):
    list_display = ("name", "list_tool_count")

    def list_tool_count(self, obj: Vendor):
        return changelist_link(
            Tool, f"{obj.tools.count()} Tools", {"vendor__id__exact": f"{obj.id}"}
        )

    list_tool_count.short_description = "Tools"


@admin.register(Tool)
class ToolAdmin(admin.ModelAdmin):
    list_display = ("flute_count", "diameter", "material", "vendor")
    list_filter = ("vendor", "material")


@admin.register(CuttingData)
class CuttingDataAdmin(admin.ModelAdmin):
    list_display = ("material", "tool", "fz_base", "vc_base")
    list_filter = ["tool", "material"]
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "tool",
                    "material",
                    ("fz_base", "fz_factor_slotting"),
                    ("vc_base", "vc_factor_slotting"),
                ),
            },
        ),
    )


@admin.register(CuttingRecipe)
class CuttingRecipeAdmin(admin.ModelAdmin):
    list_display = [
        "machine",
        "cutting_data",
        "fz_effective",
        "vc_effective",
        "cutting_data_effective",
        "ae",
        "ap",
        "cutting_power",
    ]
    readonly_fields = ["cutting_data_effective", "cutting_power"]
    list_filter = ["machine", "cutting_data__tool", "cutting_data__material"]
    fieldsets = (
        (
            "Machine, Cutter, Material selection",
            {
                "fields": ("machine", "cutting_data"),
            },
        ),
        (
            "Overrides",
            {
                "fields": (
                    ("machine_max_rpm_override", "machine_max_vf_override"),
                    ("tool_fz_override", "tool_vc_override"),
                ),
            },
        ),
        (
            "Feeds and speeds",
            {
                "fields": ("cutting_data_effective",),
            },
        ),
        (
            "Cutting forces",
            {
                "fields": ("ae", "ap", "phi_selection", "cutting_power"),
            },
        ),
    )
