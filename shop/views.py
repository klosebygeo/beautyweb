from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class ShopTemplateView(TemplateView):
    template_name = 'shop/list_of_products.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = {
            'product1': {
                'name': 'Sampon par uscat si deteriorat',
                'price': '255',
                'quantitity':'1000',
                'description': 'Pentru uz zilnic.',
                'image':'../static/img/sampon1.jpg',
            },
            'product2': {
                'name': 'Sampon par vopsit',
                'price': 225,
                'quantitity': '1000',
                'description': 'Pentru uz zilnic.',
                'image': '../static/img/sampon2.jpg',
            },
            'product3': {
                'name': 'Sampon pentru par gras',
                'price': 299,
                'description': 'Uz zilnic',
                'image': '../static/img/sampon3.jpg',
            },
            'product4': {
                'name': 'Sampon pentru par gras',
                'price': 299,
                'description': 'Uz zilnic',
                'image': '../static/img/sampon4.jpg',
            },
            'product5': {
                'name': 'Sampon pentru par gras',
                'price': 299,
                'description': 'Uz zilnic',
            },
            'product6': {
                'name': 'Sampon pentru par gras',
                'price': 299,
                'description': 'Uz zilnic',
            },
            'product7': {
                'name': 'Sampon pentru par gras',
                'price': 299,
                'description': 'Uz zilnic',
            },
            'product8': {
                'name': 'Sampon pentru par gras',
                'price': 299,
                'description': 'Uz zilnic',
            },
            'product9': {
                'name': 'Sampon pentru par gras',
                'price': 299,
                'description': 'Uz zilnic',
            }
        }
        context['products'] = products
        return context
