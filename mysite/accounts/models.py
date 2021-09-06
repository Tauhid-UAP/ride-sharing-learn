from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class GeneralUser(AbstractUser):
    is_rider = models.BooleanField(default=False)
    is_driver = models.BooleanField(default=False)
    is_activated = models.BooleanField(default=False)

class Driver(models.Model):
    generaluser = models.OneToOneField(to=GeneralUser, blank=False, null=False, on_delete=models.CASCADE)
    license_credentials = models.CharField(max_length=20, blank=False, null=False)