from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView, TemplateView

from employee.models import Employee
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


def rezervare(request):
    all_services = Service.objects.all()
    return render(request, 'programari/rezervare.html', {'all_services': all_services})


class RezervareProgramareView(TemplateView):
    template_name = 'programari/rezervare_programare.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employees'] = Employee.objects.all()
        return context


