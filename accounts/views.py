from django.shortcuts import render,redirect
from django.views.generic import CreateView,FormView,TemplateView
from .forms import *
from .models import *
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
# Create your views here.

class Reg(CreateView):
    template_name="reg.html"
    form_class=RegForm
    model=CustUser
    success_url=reverse_lazy('log')



class LogView(FormView):
    template_name="log.html"
    form_class=LogForm
    def post(self,request,*args,**kwargs):
        formlog=LogForm(data=request.POST)
        if formlog.is_valid():
            un=formlog.cleaned_data.get("username")
            ps=formlog.cleaned_data.get("password")
            user=authenticate(request,username=un,password=ps)
            if user:
                login(request,user)
                if request.user.is_superuser == True:
                    return redirect("sa")
            else:
                 return render(request,"log.html",{"form":formlog})  
        else:
            return render(request,"log.html",{"form":formlog}) 
         
class LogAdminView(FormView):
    template_name="log.html"
    form_class=LogForm
    def post(self,request,*args,**kwargs):
        formlog=LogForm(data=request.POST)
        if formlog.is_valid():
            un=formlog.cleaned_data.get("username")
            ps=formlog.cleaned_data.get("password")
            user=authenticate(request,username=un,password=ps)
            if user:
                login(request,user)
                if request.user.usertype == 'Admin':
                    return redirect("ah")
                else:
                    return redirect('uh')
            else:
                 return render(request,"log.html",{"form":formlog})  
        else:
            return render(request,"log.html",{"form":formlog})  
 
        

class MainHome(TemplateView):
    template_name="mainhom.html"        