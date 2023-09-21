from django import forms
from .models import Auditor

class AuditorForm(forms.ModelForm):
  class Meta:
    model = Auditor
    fields = '__all__'