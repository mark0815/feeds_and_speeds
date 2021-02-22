from django.contrib import admin
from .models import (
    Drill,
    DrillData,
    DrillRecipe,
)


@admin.register(Drill)
class DrillAdmin(admin.ModelAdmin):
    list_display = ("diameter", "material", "drill_type")
    list_filter = ("material", "drill_type")


@admin.register(DrillData)
class DrillDataAdmin(admin.ModelAdmin):
    list_display = ("drill", "material", "f", "vc")
    list_filter = ("drill", "material")


@admin.register(DrillRecipe)
class DrillRecipeAdmin(admin.ModelAdmin):
    list_display = (
        "drill_data",
        "rpm_override",
        "vf_override",
        "cutting_params_rpm",
        "cutting_params_vf",
    )
    readonly_fields = ["cutting_params_rpm", "cutting_params_vf"]
