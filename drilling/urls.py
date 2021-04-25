""" URL configuration """
from django.urls import include, path
from rest_framework import routers

from .views import DrillViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r"drills", DrillViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
