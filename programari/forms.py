from django import forms
from django.forms import TextInput, Select

from programari.models import Service


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = [
            'name_of_service', 'price', 'employee'
        ]
        widgets = {
            "name_of_service": TextInput(attrs={'placeholder': 'Name of service', 'class': 'form-control'}),
            "price": TextInput(attrs={'placeholder': 'Price', 'class': 'form-control'}),
            "employee": Select(attrs={'class': 'form-select'})
        }

class ServiceUpdateForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = [
            'name_of_service', 'price', 'employee'
        ]
        widgets = {
            "name_of_service": TextInput(attrs={'placeholder': 'Name of service', 'class': 'form-control'}),
            "price": TextInput(attrs={'placeholder': 'Price', 'class': 'form-control'}),
            "employee": Select(attrs={'class': 'form-select'})
        }