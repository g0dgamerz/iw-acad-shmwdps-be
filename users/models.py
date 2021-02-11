from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    GENDER_CHOICES = (( 0, 'MALE' ),( 1, "FEMALE" ), (2, "OTHER"))
    gender = models.IntegerField(choices=GENDER_CHOICES, default=2)
    image = models.FileField(upload_to="profile/",null=True,blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Staff(models.Model):
    user = models.OneToOneField(to=CustomUser, on_delete=models.CASCADE)
    department = models.CharField(max_length=50)
    contact_no = models.PositiveIntegerField()

    class Meta:
        abstract = True

class Doctor(Staff):
    specialist_of = models.CharField(max_length=100)
    #TODO: add more

class Nurse(Staff):
    pass

class Patient(models.Model):
    #TODO: Disease foreign key.
    in_hospital = models.BooleanField()
    #TODO: room id

