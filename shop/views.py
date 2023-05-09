from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class ShopTemplateView(TemplateView):
    template_name = 'shop/list_of_products.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = {
            'product1': {
                'name': 'Product 1',
                'price': 10.99,
                'description': 'This is the first product.',
            },
            'product2': {
                'name': 'Product 2',
                'price': 19.99,
                'description': 'This is the second product.',
            },
            'product3': {
                'name': 'Product 3',
                'price': 5.99,
                'description': 'This is the third product.',
            },
        }
        context['products'] = products
        return context
