from django.urls import path

from .views import RegisterProduct, AllProducts, add_to_cart, CartView

urlpatterns = [
    path('addcart/<int:id_p>/', add_to_cart, name='addcart'),
    path('viewcart/', CartView.as_view(), name='view-cart'),
    path('', AllProducts.as_view(), name='get-cart-user'),
]
