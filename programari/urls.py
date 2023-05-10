from django.urls import path

from programari import views

urlpatterns = [
    path('creare_serviciu/', views.AppointmentCreateView.as_view(), name='creare-serviciu')
]