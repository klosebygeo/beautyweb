import random
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail, EmailMessage

from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views.generic import CreateView

from beautyweb.settings import EMAIL_HOST_USER
from userextend.forms import UserForm


# Create your views here.
class UserCreateView(CreateView):
    template_name = 'userextend/create_user.html'
    model = User
    form_class = UserForm

    # success_url = reverse_lazy('homepage') # DACA FOLOSESC def form_valid(self, form) nu mai am nevoie de success_url

    def form_valid(self, form):
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.first_name = new_user.first_name.title()
            new_user.username = f'{new_user.first_name.lower()}{new_user.last_name.lower()}_{random.randint(100000, 999999)}'
            new_user.save()

            # Trimit mail fara template

            subject = 'Felicitari! Ai un cont nou in aplicatie!'
            message = f'Hello, {new_user.first_name} {new_user.last_name}. Username-ul tau este {new_user.username}'
            send_mail(subject, message, EMAIL_HOST_USER, [new_user.email])

            # TRIMIT mail CU template
            details = {
                'fullname': f'{new_user.first_name} {new_user.last_name}',
                'username': new_user.username
            }
            subject = 'Felicitari! Ai un cont nou noi in aplicatie!'
            message = get_template('mail.html').render(details)
            mail = EmailMessage(
                subject,
                message,
                EMAIL_HOST_USER,
                [new_user.email]
            )
            mail.content_subtype = 'html'
            mail.send()

        return redirect('login')
