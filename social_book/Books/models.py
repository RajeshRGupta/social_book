from django.db import models
from UserAccounts.models import *
# Create your models here.


class Books(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    book_name=models.CharField(max_length=250,blank=True,null=True)