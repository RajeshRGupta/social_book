from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date
from .manager import UserManager

# Create your models here.

class User(AbstractUser):
    username=None
    full_name=models.CharField(max_length=100,null=False,blank=False)
    email=models.EmailField(unique=True)
    public_visibility = models.BooleanField(default=True)
    birth_year = models.IntegerField(null=True, blank=True)
    address = models.TextField(null=True, blank=True
    @property
    def age(self):
        if self.birth_year:
            current_year = date.today().year
            return current_year - self.birth_year
        return None
    def name(self):
        return self.first_name + ' ' + self.last_name
    
    objects=UserManager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['full_name','birth_year']
    
    def __str__(self):
        return self.email

