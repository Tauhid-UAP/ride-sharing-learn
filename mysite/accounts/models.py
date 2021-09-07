from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class GeneralUser(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'Rider'),
        (2, 'Driver')
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=1)
    license_credentials = models.CharField(max_length=20, null=True, blank=True, default=None)
    is_activated = models.BooleanField(default=False)