from django.views.generic import ListView, DetailView
from .models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'shop/list_of_products.html'
    context_object_name = 'products'
    ordering = ['name']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.all()
        context['products'] = products
        return context


class ParListView(ListView):
    model = Product
    template_name = 'shop/list_of_products.html'
    ordering = ['name']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.filter(tip_produs=1).all()
        context['products'] = products
        return context


class BarbaListView(ListView):
    model = Product
    template_name = 'shop/list_of_products.html'
    ordering = ['name']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.filter(tip_produs=2).all()
        context['products'] = products
        return context


class AccesoriiListView(ListView):
    model = Product
    template_name = 'shop/list_of_products.html'
    ordering = ['name']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.filter(tip_produs=3).all()
        context['products'] = products
        return context

class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['product_description'] = self.object.description
        return context
