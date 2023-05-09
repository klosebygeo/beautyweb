from django.urls import path

from employee import views

urlpatterns = [
    path('create_employee/', views.EmployeeCreateView.as_view(), name='create-employee'),
    path('list_of_employees/', views.EmployeeListView.as_view(), name='list-of-employees'),
    path('update_employee/<int:pk>/', views.EmployeeUpdateView.as_view(), name='update-employee'),
    path('delete_employee/<int:pk>/', views.EmployeeDeleteView.as_view(), name='delete-employee'),
    path('details_employee/<int:pk>/', views.EmployeeDetailView.as_view(), name='details-employee'),
    path('deactivate_employee/<int:pk>/',views.deactivate_employee, name='deactivate-employee')
]