from django.db import models
from machinist_toolbox.constants import TOOL_MATERIAL_CARBIDE, TOOL_MATERIAL_CHOICES
from .constants import DRILL_TYPE_CHOICES, DRILL_TYPE_SPIRAL_DRILL


class Drill(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    flute_count = models.PositiveIntegerField()
    flute_length = models.FloatField(verbose_name="Flute length (mm)")
    diameter = models.FloatField(verbose_name="Diameter (mm)")
    tip_angle = models.FloatField(verbose_name="Tip angle")
    material = models.CharField(
        max_length=10, choices=TOOL_MATERIAL_CHOICES, default=TOOL_MATERIAL_CARBIDE
    )
    drill_type = models.CharField(
        max_length=20, choices=DRILL_TYPE_CHOICES, default=DRILL_TYPE_SPIRAL_DRILL
    )

    def __str__(self):
        return f"{self.diameter}mm {self.flute_count}fl {self.get_material_display()} ({self.get_drill_type_display()})"

    class Meta:
        ordering = ("name",)
