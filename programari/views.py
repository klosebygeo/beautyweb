from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView, TemplateView

from employee.models import Employee
from programari.models import Service, RezervareServicii
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


def rezerva_servicii(request):
    if request.POST and request.user.is_authenticated:
        current_user_id=request.user.id
        services_ids = [int(item) for item in dict(request.POST) if item!='csrfmiddlewaretoken']
        for service_id in services_ids:
            serviciu=RezervareServicii(id_service_id=service_id, id_user=current_user_id)
            serviciu.save()
        all_employees = Employee.objects.all()
        return render(request, 'programari/rezervare_programare.html', {'employees': all_employees})
    return HttpResponseRedirect(reverse("login"))

    # de inserat in modelul de mai sus lista de all_services

class RezervareProgramareView(CreateView):
    template_name = 'programari/rezervare_programare.html'
    def post(self):
        pass

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employees'] = Employee.objects.all()
        return context


