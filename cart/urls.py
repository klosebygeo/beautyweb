from django.urls import path

from cart import views

urlpatterns = [
     path('addcart/<int:user>/<int:id_p>/', views.RegisterProduct.as_view(), name='addcart'),
     path('', views.AllProducts.as_view(), name='get-cart-user'),

]