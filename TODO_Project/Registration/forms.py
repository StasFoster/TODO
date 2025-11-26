from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from . import models


class Registration_Form(UserCreationForm):
    class Meta:
        model = models.MyUser
        fields = ("username", "password1", "password2")

class Login_Form(AuthenticationForm):
    pass


