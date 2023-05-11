from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from programari.models import Service
from programari.forms import ServiceForm


class ServiceCreateView(CreateView):
    template_name = 'programari/create_service.html'
    model = Service
    form_class = ServiceForm
    success_url = reverse_lazy('homepage')

class ServiceListView(ListView):
    template_name = 'programari/list_of_services.html'
    model = Service
    context_object_name = 'all_services'

    def get_queryset(self):
        return Service.objects.all()

