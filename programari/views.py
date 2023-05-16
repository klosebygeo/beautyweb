from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from programari.models import Service
from programari.forms import ServiceForm, ServiceUpdateForm


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


class ServiceUpdateView(UpdateView):
    template_name = 'programari/update_service.html'
    model = Service
    form_class = ServiceUpdateForm
    success_url = reverse_lazy('list-of-services')


class ServiceDeleteView(DeleteView):
    template_name = 'programari/delete_service.html'
    model = Service
    success_url = reverse_lazy('list-of-services')


class ServiceDetailView(DetailView):
    template_name = 'programari/details_service.html'
    model = Service
    success_url = reverse_lazy('list-of-services')


class Rezervare(ListView):
    template_name = 'programari/rezervare.html'
    model = Service
    context_object_name = 'all_services'
    success_url = reverse_lazy('homepage')
