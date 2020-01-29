from django.urls import path, include
from rest_framework import routers
from .views import CulinaryViewSet, RegionViewSet

router = routers.DefaultRouter()
router.register('culinary', CulinaryViewSet)
router.register('region', RegionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]