from django.urls import path

from cart import views

urlpatterns = [
     path('', views.CartView.as_view(), name='addcart'),
]