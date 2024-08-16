from django.contrib import admin
from .models import *

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display=['user','book','book_name','b_description','b_cost','b_year_publish','b_visibility']
    
    
admin.site.register(Books,BookAdmin)