from django.conf import settings
from django.db import models
import uuid

# Create your models here.
class Department(models.Model):
    name=models.TextField(max_length=200)

    def __str__(self):
        return self.name
    
class Time(models.Model):
    time=models.TextField(max_length=10)

    def __str__(self):
        return self.time

    
class Doctor(models.Model):
    name=models.TextField(max_length=200)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)


class Appoinment(models.Model):
    owner_user=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    STATUS=[
        ('pending','Pending'),
        ('accept','Accept'),
        ('Reject','Reject'),
    ]
    status=models.CharField(max_length=100,choices=STATUS,default=STATUS[0])
    name=models.TextField(max_length=200)
    department=models.TextField(max_length=200)
    date=models.DateField()
    Time=models.TextField(max_length=10)
    phone=models.IntegerField(default=0)
    msg=models.TextField(max_length=200)

    def __str__(self):
        return self.name + self.department