""" URL configuration """
from django.urls import include, path
from rest_framework import routers

from .views import MaterialClassViewSet, MaterialViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r"material_classes", MaterialClassViewSet)
router.register(r"materials", MaterialViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
