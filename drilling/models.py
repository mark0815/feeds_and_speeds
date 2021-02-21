from django.db import models
from machinist_toolbox.constants import TOOL_MATERIAL_CARBIDE, TOOL_MATERIAL_CHOICES
from .constants import DRILL_TYPE_CHOICES, DRILL_TYPE_SPIRAL_DRILL
from math import sin, asin, pi
import typing as t


class Drill(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    flute_count = models.PositiveIntegerField(default=2)
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


class DrillData(models.Model):
    drill = models.ForeignKey(Drill, on_delete=models.CASCADE)
    material = models.ForeignKey("materials.Material", on_delete=models.CASCADE)
    f = models.FloatField(verbose_name="f", help_text="f in mm/revolution")
    vc = models.FloatField(verbose_name="vc", help_text="vc in m/min")

    def __str__(self) -> str:
        return f"{self.drill} {self.material}"

    class Meta:
        verbose_name = "Drill Data"
        verbose_name_plural = "Drill Data"
        ordering = ("material", "drill")


class DrillRecipe(models.Model):
    drill_data = models.ForeignKey(DrillData, on_delete=models.CASCADE)
    rpm_override = models.PositiveIntegerField(
        verbose_name="RPM Override", null=True, blank=True
    )
    vf_override = models.FloatField(verbose_name="Vf Override", null=True, blank=True)

    class Meta:
        verbose_name = "Drill Recipe"
        verbose_name_plural = "Drill Recipies"

    @property
    def cutting_params(self) -> t.Tuple[float, float]:
        rpm = (self.drill_data.vc * 1000) / (pi * self.drill_data.drill.diameter)
        vf = self.drill_data.f * rpm
        if self.rpm_override and rpm > self.rpm_override:
            rpm = self.rpm_override
            vf = self.drill_data.f * self.rpm_override
        if self.vf_override and vf > self.vf_override:
            vf = self.vf_override
            rpm = vf / self.drill_data.f
        return (rpm, vf)

    @property
    def cutting_params_rpm(self) -> float:
        return self.cutting_params[0]

    @property
    def cutting_params_vf(self) -> float:
        return self.cutting_params[1]
