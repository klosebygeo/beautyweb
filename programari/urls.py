from django.urls import path

from programari import views

urlpatterns = [
    path('creare_serviciu/', views.ServiceCreateView.as_view(), name='creare-serviciu'),
    path('list_of_services/', views.ServiceListView.as_view(), name='list-of-services')
]