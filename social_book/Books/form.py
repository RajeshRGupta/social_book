from django.forms import ModelForm
from django.forms.widgets import FileInput
from .models import *


class BookForm(ModelForm):
    class Meta:
        model = Books
        fields = '__all__'
        exclude=['user',]
        widgets={
            'book':FileInput(),
        }
    