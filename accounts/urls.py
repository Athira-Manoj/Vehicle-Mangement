from django.urls import path
from .views import *

urlpatterns = [
    path('reg/',Reg.as_view(),name="reg"),
    path('sadmin/',LogView.as_view(),name='logsd'),
    path('useradmin/',LogAdminView.as_view(),name='aduser')
]

