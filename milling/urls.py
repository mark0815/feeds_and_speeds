from django.urls import path, include
from rest_framework import routers
from .views import (
    CuttingDataViewSet,
    MachineViewSet,
    VendorViewSet,
    ToolViewSet,
)

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r"cutting_data", CuttingDataViewSet)
router.register(r"machines", MachineViewSet)
router.register(r"vendors", VendorViewSet)
router.register(r"tools", ToolViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
