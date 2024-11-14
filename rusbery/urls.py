from django.urls import path, include
from rusbery.views import *
from rest_framework import routers

app_name = "parking"

router = routers.DefaultRouter()

router.register("parking-spot", Parking_SpotViewSet)
router.register("parking-statistics", Parking_StatisticsViewSet)
router.register("parking-lot", Parking_LotViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
