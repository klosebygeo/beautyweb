from django.urls import path

from shop import views

urlpatterns = [
    path('shop/',views.ProductListView.as_view(), name='shop'),
    path('shop/',views.BarbaListView.as_view(), name='barba'),
    path('shop/',views.AccesoriiListView.as_view(), name='accesorii'),
    path('shop/ingrijire_par',views.ShopTemplateView.as_view(), name='par'),
    path('shop/ingrijire_barba',views.BarbaTemplateView.as_view(), name='barba'),
    path('shop/accesorii',views.AccesoriiTemplateView.as_view(), name='accesorii'),
]
