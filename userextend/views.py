# import random
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# from django.core.mail import send_mail, EmailMessage
#
# from django.shortcuts import render, redirect
# from django.template.loader import get_template
# from django.urls import reverse_lazy
# from django.views.generic import CreateView
#
# from beautyweb.settings import SENDGRID_API_KEY
# from userextend.forms import UserForm
# import sendgrid
# from sendgrid.helpers.mail import *
#
# # Create your views here.
# class UserCreateView(CreateView):
#     template_name = 'userextend/create_user.html'
#     model = User
#     form_class = UserForm
#
#     # success_url = reverse_lazy('homepage') # DACA FOLOSESC def form_valid(self, form) nu mai am nevoie de success_url
#
#     def form_valid(self, form):
#         if form.is_valid():
#             new_user = form.save(commit=False)
#             new_user.first_name = new_user.first_name.title()
#             new_user.username = f'{new_user.first_name.lower()}{new_user.last_name.lower()}_{random.randint(100000, 999999)}'
#             new_user.save()
#
#         sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)
#         from_email = Email("beautywebdjango@gmail.com")
#
#         to_email = To("georgian.ivan95@gmail.com")
#         subject = 'Felicitari! Ai un cont nou in aplicatie!'
#         content = f'Hello, {new_user.first_name} {new_user.last_name}. Username-ul tau este {new_user.username}'
#         mail = Mail(from_email, to_email, subject, content, [new_user.email])
#         response = sg.client.mail.send.post(request_body=mail.get())
#
#         return redirect('login')
import random

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView
from django.core.mail import send_mail, EmailMessage

from django.shortcuts import render, redirect
from django.template.loader import get_template, render_to_string
from django.urls import reverse_lazy
from django.views.generic import CreateView

from beautyweb.settings import SENDGRID_API_KEY
from userextend.forms import UserForm
import sendgrid
from sendgrid.helpers.mail import *

class UserCreateView(CreateView):
    template_name = 'userextend/create_user.html'
    model = User
    form_class = UserForm

    def form_valid(self, form):
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.first_name = new_user.first_name.title()
            new_user.username = f'{new_user.first_name.lower()}{new_user.last_name.lower()}_{random.randint(100000, 999999)}'
            new_user.save()

            sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)
            from_email = Email("beautywebdjango@gmail.com")
            to_email = To(new_user.email)
            subject = 'Felicitari! Ai un cont nou in aplicatie!'

            # Incarca template-ul e-mailului
            context = {'user':new_user
                       }
            content = render_to_string('mail.html',context)

            # Genereaza continutul e-mailului din template
            #content = template.render({'first_name': new_user.first_name, 'last_name': new_user.last_name, 'username': new_user.username})

            # Construieste obiectul Mail si adauga continutul
            mail = Mail(from_email, to_email, subject)
            mail.add_content(Content("text/html", content))

            # Trimite e-mailul
            sg.client.mail.send.post(request_body=mail.get())

        return redirect('login')


class ExtendedUserLogOut(LogoutView):
    template_name = "registration/login.html"