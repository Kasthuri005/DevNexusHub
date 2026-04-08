from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True)

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="customuser_set",  # Prevents clash with default User
        blank=True
    )
    
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="customuser_set",  # Prevents clash with default User
        blank=True
    )
