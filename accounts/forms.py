from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class RegForm(UserCreationForm):
    class Meta:
        model=CustUser
        fields=['first_name','last_name','gender','email','phone','usertype','username','password1','password2']
        widgets={
            "first_name":forms.TextInput(attrs={"class":"form-control","placeholder":"Firstname"}),
            "last_name":forms.TextInput(attrs={"class":"form-control","placeholder":"Lastname"}),
            "gender":forms.RadioSelect(),
            "phone":forms.NumberInput(attrs={"class":"form-control","placeholder":"Phone"}),
            "email":forms.EmailInput(attrs={"class":"form-control","placeholder":"Email"}),
            "username":forms.TextInput(attrs={"class":"form-control","placeholder":"Username"}),
            "password1":forms.PasswordInput(attrs={"class":"form-control","placeholder":"Password"}),
            "password2":forms.PasswordInput(attrs={"class":"form-control","placeholder":"Confirm Password"})           
        }
        
class LogForm(forms.Form):
    username=forms.CharField(max_length=50,widget=forms.TextInput(attrs={"placeholder":"Username","class":"form-control"}))
    password=forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={"placeholder":"Password","class":"form-control"}))
