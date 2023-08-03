from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import TemplateView,UpdateView
from superadmin.models import *
from superadmin.forms import *
from django.urls import reverse_lazy

# Create your views here.


class VehicleAdView(TemplateView):
    template_name="ahome.html"
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["data"]=Vehicle.objects.all()
        return context 


class VehicleAdUpdate(UpdateView):
    template_name="adupdate.html"
    model=Vehicle
    form_class=VehicleForm
    success_url=reverse_lazy('ah')

