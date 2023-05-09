from django.urls import path

from shop import views

urlpatterns = [
    path('shop/',views.ShopTemplateView.as_view(), name='shop')
]
