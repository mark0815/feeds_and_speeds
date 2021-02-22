from machinist_toolbox.constants import TOOL_MATERIAL_CARBIDE, TOOL_MATERIAL_CHOICES
from django.db import models


class Vendor(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = "Tool Vendor"
        verbose_name_plural = "Tool Vendors"
        ordering = ("name",)


class Tool(models.Model):
    vendor = models.ForeignKey(
        Vendor, on_delete=models.CASCADE, related_name="tools", null=True
    )
    description = models.TextField(null=True, blank=True)
    flute_count = models.PositiveIntegerField()
    flute_length = models.FloatField(verbose_name="Flute length (mm)")
    diameter = models.FloatField(verbose_name="Diameter (mm)")
    cutting_edge_angle = models.FloatField(
        verbose_name="Cutting edge angle KAPR (degree)", default=90
    )
    material = models.CharField(
        max_length=10, choices=TOOL_MATERIAL_CHOICES, default=TOOL_MATERIAL_CARBIDE
    )

    def __str__(self):
        return f"{self.diameter}mm {self.flute_count}fl {self.get_material_display()} ({self.vendor})"

    class Meta:
        ordering = ("vendor", "diameter")
