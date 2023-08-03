from django.urls import path
from .views import *

urlpatterns=[
    path('ahomes/',VehicleAdView.as_view(),name="ah"),
    path('adupd/<int:pk>/',VehicleAdUpdate.as_view(),name='adupd')
]