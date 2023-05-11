from django.urls import path

from programari import views

urlpatterns = [
    path('creare_serviciu/', views.ServiceCreateView.as_view(), name='creare-serviciu')
]