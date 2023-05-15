from django.views.generic import TemplateView, ListView
from .models import Product, Product_accesory


class ShopTemplateView(TemplateView):
    template_name = 'shop/list_of_products.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.filter(tip_produs=1).all()
        context['products'] = products
        return context


class BarbaTemplateView(TemplateView):
    template_name = 'shop/ingrijire_barba.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.filter(tip_produs=2).all()
        context['products'] = products
        return context


class AccesoriiTemplateView(TemplateView):
    template_name = 'shop/accesorii.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.filter(tip_produs=3).all()
        context['products'] = products
        return context


class ProductListView(ListView):
    model = Product
    template_name = 'shop/list_of_products.html'
    context_object_name = 'products'
    ordering = ['name']

# def get_all_products(request):
#     template_name = 'shop/list_of_products.html'
#     products=Product.objects.all().order_by('name')
#     return render(request, template_name, {'products':products})
#

class BarbaListView(ListView):
    model = Product
    template_name = 'shop/ingrijire_barba.html'
    context_object_name = 'products'
    ordering = ['name']

class AccesoriiListView(ListView):
    model = Product_accesory
    template_name = 'shop/accesorii.html'
    context_object_name = 'products'
    ordering = ['name']


