from django.views.generic import TemplateView, ListView
from .models import Product


class ShopTemplateView(TemplateView):
    template_name = 'shop/list_of_products.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.all()
        context['products'] = products
        return context


class BarbaTemplateView(TemplateView):
    template_name = 'shop/ingrijire_barba.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.all()
        context['products'] = products
        return context


class AccesoriiTemplateView(TemplateView):
    template_name = 'shop/accesorii.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.all()
        context['products'] = products
        return context


class ProductListView(ListView):
    model = Product
    template_name = 'shop/list_of_products.html'
    context_object_name = 'products'
