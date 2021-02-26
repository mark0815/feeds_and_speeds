from django.http.response import HttpResponse
from machinist_toolbox.admin_helper import changelist_link, changelist_url
from milling.models.tool_table import ToolTableEntry
from django.contrib import admin
from django.urls import path
from django.template import loader


@admin.register(ToolTableEntry)
class ToolTableEntryAdmin(admin.ModelAdmin):
    list_display = ("t", "z", "d", "name", "tool")
    change_list_template = "admin/tool_table_change_list.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path("export_linuxcnc/", self.export_linuxcnc),
        ]
        return my_urls + urls

    def export_linuxcnc(self, request):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="tool.tbl"'

        t = loader.get_template("admin/export_linuxcnc.txt")
        c = {"data": ToolTableEntry.objects.all()}
        response.write(t.render(c))
        return response
