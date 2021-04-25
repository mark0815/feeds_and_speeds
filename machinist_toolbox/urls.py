""" URL configuration """

from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("materials/", include("materials.urls")),
    path("milling/", include("milling.urls")),
    path("drilling/", include("drilling.urls")),
    url(r"^$", RedirectView.as_view(url="/admin")),
]
