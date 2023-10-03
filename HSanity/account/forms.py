from django import forms
from .models import Auditor
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AuditorForm(forms.ModelForm):
    class Meta:
        model = Auditor
        fields = "__all__"

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']