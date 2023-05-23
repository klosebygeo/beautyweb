from django.urls import path

from .views import RegisterProduct, AllProducts, add_to_cart, get_cart_details

urlpatterns = [
    path('addcart/', add_to_cart, name='addcart'),
    path('viewcart/', get_cart_details, name='view-cart'),
    path('', AllProducts.as_view(), name='get-cart-user'),
]
