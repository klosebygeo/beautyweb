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
                'price': 155,
                'quantity':'500',
                'description': 'Pentru uz zilnic.',
                'image':'../static/img/sampon1.jpg',
            },
            'product2': {
                'name': 'Sampon par vopsit',
                'price': 175,
                'quantity': '500',
                'description': 'Pentru uz zilnic.',
                'image': '../static/img/sampon2.jpg',
            },
            'product3': {
                'name': 'Sampon pentru par gras',
                'price': 215,
                'quantity': '500',
                'description': 'Uz zilnic',
                'image': '../static/img/sampon3.jpg',
            },
            'product4': {
                'name': 'Sampon pentru par lipsit de volum',
                'price': 299,
                'quantity': '1000',
                'description': 'Uz zilnic',
                'image': '../static/img/sampon4.jpg',
            },
            'product5': {
                'name': 'Sampon pentru par ondulat',
                'price': 299,
                'quantity': '1000',
                'description': 'Uz zilnic',
                'image': '../static/img/sampon5.jpg',
            },
            'product6': {
                'name': 'Sampon profesional cu keratina',
                'price': 455,
                'quantity': '1000',
                'description': 'Hraneste si hidrateaza in profunzime.',
                'image': '../static/img/sampon1.jpg',
            },
            'product7': {
                'name': 'Sampon pentru par blond',
                'price': 299,
                'quantity': '1000',
                'description': 'Neutralizeaza reflexele galbene ale parului',
                'image': '../static/img/sampon4.jpg',
            },
            'product8': {
                'name': 'Sampon par vopsit',
                'price': 375,
                'quantity': '1000',
                'description': 'Pentru uz zilnic.',
                'image': '../static/img/sampon2.jpg',

            },
            'product9': {
                'name': 'Sampon pentru par gras',
                'price': 215,
                'quantity': '1000',
                'description': 'Uz zilnic',
                'image': '../static/img/sampon3.jpg',
            }
        }
        context['products'] = products
        return context
