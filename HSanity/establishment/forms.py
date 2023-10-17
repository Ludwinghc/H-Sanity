from django import forms
from .models import Establishment

class HotelForm(forms.ModelForm):
    class Meta:
        model = Establishment
        fields = '__all__'
