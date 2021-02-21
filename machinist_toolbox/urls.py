from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("materials/", include("materials.urls")),
    path("milling/", include("milling.urls")),
    path("drilling/", include("drilling.urls")),
]
