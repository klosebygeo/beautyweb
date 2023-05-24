from django.urls import path

from . import views
from .views import add_to_cart, get_cart_details, all_products, ProductDeleteView, allways_cart

urlpatterns = [
    path('addcart/', add_to_cart, name='addcart'),
    path('viewcart/', get_cart_details, name='view-cart'),
    # path('', AllProducts.as_view(), name='get-cart-user'),
    path('products/', all_products, name='get-cart-user'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),
    path('items/', allways_cart, name='always-cart'),
]
