from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    middle_name = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}: {self.username}"
    



# Create your models here.
