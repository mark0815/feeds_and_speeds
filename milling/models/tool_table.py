from django.db import models
from milling.models.tool import Tool


class ToolTableEntry(models.Model):
    """
    T1 P1 X0.0 Y0.0 Z182.0599 A0.0 B0.0 C0.0 U0.0 V0.0 W0.0 D3.0 I0.0 J0.0 Q0.0 ;3d-taster
    """

    tool = models.ForeignKey(
        Tool,
        on_delete=models.CASCADE,
        related_name="tool_table_entry",
        null=True,
        blank=True,
    )
    t = models.PositiveIntegerField()
    z = models.FloatField(
        help_text="Overall tool length (including tool holder) from spindle 0."
    )
    d = models.FloatField(
        null=False,
        blank=False,
        help_text="Tool diameter override to compensate tool wear.",
    )
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Tool Table Entry"
        verbose_name_plural = "Tool Table Entries"
        ordering = ("t",)
