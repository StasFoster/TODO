from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from . import models


class Registration_Form(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = models.MyUser
        fields = ("nickname", "username", "email", "password1", "password2")

class Login_Form(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField()


