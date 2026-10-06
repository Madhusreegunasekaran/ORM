from django.contrib import admin
from.models import Vehicle_Service
class Vehicle_ServiceAdmin(admin.ModelAdmin):
    list_display=["Vehicle_No","Owner_Name","Vehicle_Model","Service_Date","Phone_No","Service_Type","Amount","Kms_Run","Last_Service_Date"]  
admin.site.register(Vehicle_Service,Vehicle_ServiceAdmin)


