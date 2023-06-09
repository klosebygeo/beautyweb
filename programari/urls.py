from django.urls import path

from programari import views
from programari.views import rezerva_servicii

urlpatterns = [
    path('creare_serviciu/', views.ServiceCreateView.as_view(), name='creare-serviciu'),
    path('list_of_services/', views.ServiceListView.as_view(), name='list-of-services'),
    path('update_service/<int:pk>', views.ServiceUpdateView.as_view(), name='update-service'),
    path('delete_service/<int:pk>', views.ServiceDeleteView.as_view(), name='delete-service'),
    path('details_service/<int:pk>', views.ServiceDetailView.as_view(), name='details-service'),
    path('rezervare/', views.Rezervare.as_view(), name='rezervare'),
    path('rezervare/programare/', rezerva_servicii, name='rezervare-programare'),

]