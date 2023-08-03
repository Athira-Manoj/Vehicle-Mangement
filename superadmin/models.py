from django.db import models

# Create your models here.

class Vehicle(models.Model):
    number=models.CharField(max_length=20)
    options=(
        ("Two Wheelers","Two Wheelers"),
        ("Three Wheelers","Three Wheelers"),
        ("Four Wheelers","Four Wheelers"),
    )
    type=models.CharField(max_length=100,choices=options,default="Two Wheelers")
    model=models.TextField()
    description=models.TextField()
    