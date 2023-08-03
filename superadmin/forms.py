from django import forms
from .models import *


class VehicleForm(forms.ModelForm):
    class Meta:
        model=Vehicle
        fields=["number","type","model","description"]
        widgets={
            "number":forms.TextInput(attrs={"class":"form-control","placeholder":"Vehicle Number"}),
            "type":forms.RadioSelect(),
            "model":forms.TextInput(attrs={"class":"form-control","placeholder":"Vehicle Model"}),
            "description":forms.Textarea(attrs={"class":"form-control","placeholder":"Description"}),

        }