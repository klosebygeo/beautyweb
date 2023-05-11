from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from programari.models import Service
from programari.forms import ServiceForm


class ServiceCreateView(CreateView):
    template_name = 'programari/create_service.html'
    model = Service
    form_class = ServiceForm
    success_url = reverse_lazy('homepage')

