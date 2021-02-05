from django.contrib import admin
from .models import CustomUser, Doctor, Patient, Nurse
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Nurse)