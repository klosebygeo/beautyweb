from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView


class AppointmentCreateView(CreateView):
    template_name = ''
    model = ''
    form_class = ''
    success_url = reverse_lazy('homepage')

