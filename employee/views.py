


from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from employee.forms import EmployeeForm, EmployeeUpdateForm
from employee.models import Employee


# CreateView- este un view generic de la Django care ne ajuta sa ne genereze formularul in interfata
#iar datele completate in formular sa fie salvate in tabela




class EmployeeCreateView( CreateView):
    template_name = 'employee/create_employee.html' # scriem calea catre pagina html unde vor gasi formularul generat
    model = Employee
    form_class = EmployeeForm

    success_url = reverse_lazy('homepage') # il folosimt pentru a-l redirectiona pe utilizator pe o pagina in momentul

    #in care datele din formular au fost salvate

# ListView -> il folosim pentru randare/afisarea datelor dintr-o tabela

class EmployeeListView( ListView):
    template_name = 'employee/list_of_employees.html'
    model = Employee
    context_object_name = 'all_employees' # Students.objects.all()


    def get_queryset(self):
        return  Employee.objects.filter(active=True)




# UpdateView -> il folosim pentru a actualiza informatiile legate de respectiva inregistrare
class EmployeeUpdateView(UpdateView):
        template_name = 'employee/update_employee.html'
        model = Employee
        form_class = EmployeeUpdateForm
        success_url = reverse_lazy('list-of-employees')




class EmployeeDeleteView(DeleteView):
    template_name = 'employee/delete_employee.html'
    model = Employee
    success_url = reverse_lazy('list-of-employees')


# DetailView-> il folosim pentru a randa informatii legat de student


class EmployeeDetailView(DetailView):
    template_name = 'employee/details_employee.html'
    model = Employee
    permission_required = 'employee.view_employee'




def deactivate_employee(request, pk):
    # cauta studentul in tabela student si actualizeaza coloana active din True in False
    Employee.objects.filter(id=pk).update(active=False)

    return redirect('list-of-employees')

