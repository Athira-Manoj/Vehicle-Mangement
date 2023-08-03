from django.urls import path
from .views import UserHomeView

urlpatterns=[
    path('userhome/',UserHomeView.as_view(),name="uh")
]