from django.urls import path

from shop import views

urlpatterns = [
    path('',views.ProductListView.as_view(), name='shop'),
    path('barba/',views.BarbaListView.as_view(), name='barba'),
    path('accesorii/',views.AccesoriiListView.as_view(), name='accesorii'),
    path('par/',views.ParListView.as_view(), name='par'),
    path('details/<int:pk>', views.ProductDetailView.as_view(), name='details'),
    # path('delete/<int:pk>', views.ProductdeleteView.as_view(), name='delete'),
]