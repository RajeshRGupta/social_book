from django.db import models
from UserAccounts.models import *
# Create your models here.


class Books(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    book=models.FileField(upload_to='books/')
    book_name=models.CharField(max_length=250,blank=True,null=True)
    b_description=models.CharField(max_length=255,blank=True,null=True)
    b_cost=models.IntegerField(null=True,blank=True)
    b_year_publish=models.IntegerField(null=True,blank=True)
    b_visibility=models.BooleanField(default=True)