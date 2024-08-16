from rest_framework import serializers
from .models import *


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model=Books
        exclude=['user',]
