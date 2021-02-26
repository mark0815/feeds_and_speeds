from machinist_toolbox.admin_helper import changelist_link
from django.contrib import admin
from milling.models import (
    Vendor,
    Tool,
)


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
