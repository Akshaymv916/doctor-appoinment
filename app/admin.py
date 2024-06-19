from django.contrib import admin
from .models import Department,Doctor,Time,Appoinment
# Register your models here.

admin.site.register(Department)
admin.site.register(Doctor)
admin.site.register(Time)
admin.site.register(Appoinment)