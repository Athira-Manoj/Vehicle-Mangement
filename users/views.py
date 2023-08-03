from django.shortcuts import render
from django.views.generic import TemplateView
from superadmin.models import Vehicle

# Create your views here.


class UserHomeView(TemplateView):
    template_name="homeview.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["data"]=Vehicle.objects.all()
        return context