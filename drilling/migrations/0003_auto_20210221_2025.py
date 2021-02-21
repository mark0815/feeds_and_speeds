# Generated by Django 3.1.7 on 2021-02-21 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("drilling", "0002_auto_20210221_2011"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="drilldata",
            options={
                "ordering": ("material", "drill"),
                "verbose_name": "Drill Data",
                "verbose_name_plural": "Drill Data",
            },
        ),
        migrations.AlterModelOptions(
            name="drillrecipe",
            options={
                "verbose_name": "Drill Recipe",
                "verbose_name_plural": "Drill Recipies",
            },
        ),
    ]
