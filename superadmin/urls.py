from django.urls import path
from .views import *

urlpatterns=[
    path('sh/',Shome.as_view(),name='sa'),
    path('vadd/',VehicleView.as_view(),name='add'),
    path('vupd/<int:pk>/',VehicleUpdate.as_view(),name='upd'),
    path('vdel/<int:pk>/',VehicleDelete.as_view(),name='del'),

]