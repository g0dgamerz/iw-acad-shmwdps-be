from django.db import models
from users.models import Patient, Doctor

# Create your models here.
class HospitalDetail(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    description=models.TextField()
    def __str__(self):
        return self.name

class Room(models.Model):
    room_no=models.CharField(max_length=10)
    room_desc=models.TextField()

    def __str__(self):
        return self.room_no


class Bed(models.Model):
    room_no=models.ForeignKey(Room,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk) + self.room_no


class Lab(models.Model):
    patient = models.ForeignKey(Patient,on_delete=models.DO_NOTHING,blank=True, null=True)
    doctor=models.ForeignKey(Doctor,on_delete=models.DO_NOTHING,blank=True, null=True)
    date=models.DateTimeField(auto_now=True)
    amount=models.DecimalField(decimal_places=10, max_digits=100)


class Appointment(models.Model):
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    appointment_date=models.DateTimeField()
    fee=models.DecimalField(decimal_places=10,max_digits=100)

class Bill(models.Model):
    patient=models.ForeignKey(Patient,on_delete=models.DO_NOTHING,blank=True, null=True)
    appointment=models.OneToOneField(Appointment,on_delete=models.DO_NOTHING,blank=True, null=True)
    lab=models.OneToOneField(Lab,on_delete=models.DO_NOTHING,blank=True, null=True)


class Disease(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Symptoms(models.Model):
    name = models.CharField(max_length=100)
    disease=models.ManyToManyField(Disease)