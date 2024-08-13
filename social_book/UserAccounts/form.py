from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'birth_year', 'address', 'public_visibility', 'password1', 'password2')
class UserLoginForm(AuthenticationForm):
    email = forms.EmailField()
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields.pop('username')
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        if email:
            self.cleaned_data['username'] = email
        return cleaned_data
    
    
