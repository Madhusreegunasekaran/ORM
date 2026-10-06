from django.db import models
from django.contrib import admin
class Vehicle_Service(models.Model):
    Vehicle_No=models.CharField(max_length=20)
    Owner_Name=models.CharField(max_length=30)
    Vehicle_Model=models.CharField(max_length=30)
    Service_Date=models.DateField()
    Phone_No=models.CharField(max_length=10)
    Service_Type=models.CharField(max_length=30)
    Amount=models.FloatField()
    Kms_Run=models.IntegerField()
    Last_Service_Date=models.DateField(null=True)
    
    class Vehicle_ServiceAdmin(admin.ModelAdmin):
        list_display=["Vehicle_No","Owner_Name","Vehicle_Model","Service_Date","Phone_No","Service_Type","Amount","Kms_Run","Last_Service_Date"]  