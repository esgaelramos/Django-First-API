from django.db import models

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

# Create your models here.

#We re-write the model default user, but we got one login with email and not only user:

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """" MODEL DATABASE FOR USERS IN SYSTEM """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=20)
    #When user 'delete' his profile has a 'backup', because we only not show his profile, but never delete
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name
    
    def get_short_name(self):
        return self.name

    def __str__(self):
        """ RETURN STRING LIKE USER"""
        return self.email
    