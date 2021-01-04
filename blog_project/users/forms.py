from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    #user creation configuration, field in form
    class Meta:
        model = User
        fields = ['username','email','password1', 'password2'] #fields shown in form