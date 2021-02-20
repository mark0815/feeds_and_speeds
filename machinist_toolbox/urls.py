from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("materials/", include("materials.urls")),
    path("milling_calculator/", include("milling_calculator.urls")),
]
