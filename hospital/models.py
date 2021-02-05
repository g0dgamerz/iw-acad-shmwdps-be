from django.db import models

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