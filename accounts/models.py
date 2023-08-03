from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustUser(AbstractUser):
    phone=models.IntegerField(null=True)
    options=(
        ("Admin","Admin"),
        ("customer","customer")
    )
    usertype=models.CharField(max_length=100,choices=options,null=True)
    
    options=(
         ("Male","Male"),
        ("Female","Female"),
        ("Others","others")    
    )
    gender=models.CharField(max_length=500,choices=options,default="Male")
    # is_user=models.BooleanField('user status',default=False)
    # is_admin=models.BooleanField('admin status',default=False)
    
