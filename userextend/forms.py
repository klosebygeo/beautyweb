from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your first name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your last name'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your email'}),
            'username': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your username'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter your password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter your password'})


class AuthenticationNewForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter your username'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter your password'})


class PasswordChangeNewForm(PasswordChangeForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['old_password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter your Old Passowrd'})
        self.fields["new_password1"].widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter your New Passowrd'})
        self.fields["new_password2"].widget.attrs.update({'class': 'form-control', 'placeholder': 'Please re-enter your New Passowrd'})

