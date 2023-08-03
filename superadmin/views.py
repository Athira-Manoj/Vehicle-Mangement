from typing import Any, Dict
from django.shortcuts import render,redirect
from django.views.generic import CreateView,TemplateView,UpdateView,View
from .models import *
from .forms import *
from django.urls import reverse_lazy
# Create your views here.


class Shome(TemplateView):
    template_name="home.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["data"]=Vehicle.objects.all()
        return context

class VehicleView(CreateView):
    template_name="vehicle_add.html"
    model=Vehicle
    form_class=VehicleForm
    success_url=reverse_lazy('add')


class VehicleUpdate(UpdateView):
    template_name="vehicle_update.html"    
    model=Vehicle
    form_class=VehicleForm
    success_url=reverse_lazy('sa')
    pk_url_kwarg="pk"


class VehicleDelete(View):
     def get(self,request,*args,**kwargs):    
        id=kwargs.get("pk")
        vd=Vehicle.objects.get(id=id)
        vd.delete()
        return redirect('sa')     
     

     