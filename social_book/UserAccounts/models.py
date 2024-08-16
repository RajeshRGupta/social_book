from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from datetime import date,timedelta
from .manager import UserManager


# Create your models here.

class User(AbstractUser):
    username=None
    full_name=models.CharField(max_length=100,null=False,blank=False)
    email=models.EmailField(unique=True)
    public_visibility = models.BooleanField(default=True)
    birth_year = models.IntegerField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)

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
    
    
    

class OTP(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    otp_code=models.CharField(max_length=8,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    resent = models.BooleanField(default=False) 
    
    def is_valid(self):
        return timezone.now()<=self.created_at+timedelta(minutes=5)


