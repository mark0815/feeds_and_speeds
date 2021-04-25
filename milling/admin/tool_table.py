""" Tool table admin """
from django.contrib import admin
from django.http.response import HttpResponse
from django.template import loader
from django.urls import path

from milling.models.tool_table import ToolTableEntry


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

    @staticmethod
    def export_linuxcnc(_):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="tool.tbl"'

        tool_table_template = loader.get_template("admin/export_linuxcnc.txt")
        tool_table_data = {"data": ToolTableEntry.objects.all().order_by("t")}
        response.write(tool_table_template.render(tool_table_data))
        return response
