from django.urls import path

from shop import views

urlpatterns = [
    path('shop/',views.ShopTemplateView.as_view(), name='shop'),
    path('shop/ingrijire_barba',views.BarbaTemplateView.as_view(), name='barba'),
]
