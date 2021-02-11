from django.contrib import admin

from .model import HospitalDetail,Room,Bed,Lab,Appointment,Bill,Disease,Symptoms




admin.site.register(HospitalDetail)
admin.site.register(Room)
admin.site.register(Bed)
admin.site.register(Lab)
admin.site.register(Appointment)
admin.site.register(Bill)
admin.site.register(Disease)
admin.site.register(Symptoms)