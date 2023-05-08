from django import forms
from django.forms import TextInput, EmailInput, Textarea

from contact.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Please enter your first name', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Please enter your last name', 'class': 'form-control'}),
            'email': EmailInput(attrs={'placeholder': 'Please enter your email', 'class': 'form-control'}),
            'phone_number': TextInput(attrs={'placeholder': 'Please enter your phone number', 'class': 'form-control'}),
            'description': Textarea(attrs={'placeholder': 'Please enter your description', 'class': 'form-control', 'rows': 3}),
        }