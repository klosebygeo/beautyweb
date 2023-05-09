from django import forms
from django.forms import TextInput, NumberInput, EmailInput, Textarea

from employee.models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        # fields = '__all__' # preia toate fieldurile din model si in interfata va fi in ordinea declarata in fisierul models.py
        fields = ['first_name', 'last_name',
                  'age', 'email', 'description',
                  'active']  # vom specifica fieldurile pe care le vrem din modelul student in ordinea dorita

        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Please enter your first name', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Please enter your last name', 'class': 'form-control'}),
            'age': NumberInput(attrs={'placeholder': 'Please enter your age', 'class': 'form-control'}),
            'email': EmailInput(attrs={'placeholder': 'Please enter your email', 'class': 'form-control'}),
            'description': Textarea(attrs={'placeholder': 'Please enter your description', 'class': 'form-control',
                                           'rows': 3})



        }

    def clean(self):  # in cadrul acestei metode clean veti putea adauga validari pentru formualar
        cleaned_data = self.cleaned_data  # stocam un dictionar cu toate valorile completate de utilizator in formular
        get_email = cleaned_data[
            'email']  # cleaned_data.get('email') -> accesam valoarea cheii email din dictionar-> valoarea introdusa de utilizator
        check_emails = Student.objects.filter(
            email=get_email)  # cautam in tabela toti studenti care au adresa de email = cea introdusa de utilizator
        if check_emails:  # daca exista un student cu adresa de email, generaram eroare
            msg = 'Email already exists in database'
            self._errors['email'] = self.error_class([msg])


class EmployeeUpdateForm(forms.ModelForm):
    class Meta:
        model = Employee
        # fields = '__all__' # preia toate fieldurile din model si in interfata va fi in ordinea declarata in fisierul models.py
        fields = ['first_name', 'last_name',
                  'age', 'email', 'description',
                  'active']  # vom specifica fieldurile pe care le vrem din modelul student in ordinea dorita

        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Please enter your first name', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Please enter your last name', 'class': 'form-control'}),
            'age': NumberInput(attrs={'placeholder': 'Please enter your age', 'class': 'form-control'}),
            'email': EmailInput(attrs={'placeholder': 'Please enter your email', 'class': 'form-control'}),
            'description': Textarea(attrs={'placeholder': 'Please enter your description', 'class': 'form-control',
                                           'rows': 3})
        }