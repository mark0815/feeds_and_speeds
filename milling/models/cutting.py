from ..constants import PHI_SELECTION_CENTER, PHI_SELECTION_CHOICES
from django.db import models
import typing as t
from .machine import Machine
from .tool import Tool
from .. import calculator


class CuttingData(models.Model):
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE)
    material = models.ForeignKey("materials.Material", on_delete=models.CASCADE)
    fz_base = models.FloatField(
        verbose_name="fz (base)", help_text="fz at ae=0.5d and ap=1d"
    )
    vc_base = models.FloatField(
        verbose_name="vc (base)", help_text="vc at ae=0.5d and ap=1d"
    )
    fz_factor_slotting = models.FloatField(
        verbose_name="fz factor slotting",
        help_text="fz factor for slotting operations",
        default=1.0,
    )
    vc_factor_slotting = models.FloatField(
        verbose_name="vc factor slotting",
        help_text="vc factor for slotting operations",
        default=1.0,
    )

    def __str__(self) -> str:
        return f"{self.tool} {self.material}"

    class Meta:
        verbose_name = "Cutting Data"
        verbose_name_plural = "Cutting Data"
        ordering = ("material", "tool")


class CuttingRecipe(models.Model):
    cutting_data = models.ForeignKey(CuttingData, on_delete=models.CASCADE)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)

    machine_max_rpm_override = models.PositiveIntegerField(
        verbose_name="Max spindle RPM override", null=True, blank=True
    )
    machine_max_vf_override = models.FloatField(
        verbose_name="Max cutting speed override", null=True, blank=True
    )
    tool_fz_override = models.FloatField(
        verbose_name="fz override", null=True, blank=True
    )
    tool_vc_override = models.FloatField(
        verbose_name="vc override", null=True, blank=True
    )
    ae = models.FloatField(verbose_name="ae (mm)", null=True, blank=True)
    ap = models.FloatField(verbose_name="ap (mm)", null=True, blank=True)
    phi_selection = models.CharField(
        max_length=2, choices=PHI_SELECTION_CHOICES, null=True, blank=True
    )

    class Meta:
        verbose_name = "Cutting Recipe"
        verbose_name_plural = "Cutting Recipies"

    @property
    def fz_effective(self) -> float:
        if self.tool_fz_override:
            return self.tool_fz_override
        if self.ae and self.ae >= self.cutting_data.tool.diameter:
            return self.cutting_data.fz_base * self.cutting_data.fz_factor_slotting
        else:
            return self.cutting_data.fz_base

    @property
    def vc_effective(self) -> float:
        if self.tool_vc_override:
            return self.tool_vc_override
        if self.ae and self.ae >= self.cutting_data.tool.diameter:
            return self.cutting_data.vc_base * self.cutting_data.vc_factor_slotting
        else:
            return self.cutting_data.vc_base

    @property
    def max_rpm(self) -> float:
        return (
            self.machine_max_rpm_override
            if self.machine_max_rpm_override
            else self.machine.max_rpm
        )

    @property
    def max_vf(self) -> float:
        return (
            self.machine_max_vf_override
            if self.machine_max_vf_override
            else self.machine.max_vf
        )

    @property
    def cutting_data_effective(self) -> t.Tuple[float, float]:
        # calculate f&s based on tool
        return calculator.calculate_rpm_vf(
            vc=self.vc_effective,
            fz=self.fz_effective,
            tool_diameter=self.cutting_data.tool.diameter,
            tool_flute_count=self.cutting_data.tool.flute_count,
            max_rpm=self.max_rpm,
            max_vf=self.max_vf,
        )

    @property
    def cutting_power(self) -> t.Optional[float]:
        """ Cutting Power in kW """
        if self.ae and self.ap and self.phi_selection:
            p = calculator.final_pmot(
                mittig=(self.phi_selection == PHI_SELECTION_CENTER),
                a_e=self.ae,
                a_p=self.ap,
                d_c=self.cutting_data.tool.diameter,
                z_cutter=self.cutting_data.tool.flute_count,
                k_apr=self.cutting_data.tool.cutting_edge_angle,
                v_c=self.vc_effective,
                m_c=self.cutting_data.material.mc,
                k_c_1_1=self.cutting_data.material.kc_1_1,
                f_z=self.fz_effective,
            )
            return round(p, 4)
