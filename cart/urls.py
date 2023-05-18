from django.urls import path
from .views import RegisterProduct, AllProducts

urlpatterns = [
     path('addcart/<int:user_id>/<int:id_p>/', RegisterProduct.as_view(), name='addcart'),
     path('', AllProducts.as_view(), name='get-cart-user'),
]