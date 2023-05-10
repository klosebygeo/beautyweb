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
                'description': 'Netezeste si regenereaza parul',
                'image':'../static/img/sampon1.jpg',
            },
            'product2': {
                'name': 'Sampon par vopsit',
                'price': 175,
                'quantity': '500',
                'description': 'Hidratare, Protecția culorii',
                'image': '../static/img/sampon2.jpg',
            },
            'product3': {
                'name': 'Sampon pentru par gras',
                'price': 215,
                'quantity': '500',
                'description': 'Curata eficient scalpul',
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
                'description': 'Revitalizeaza si hraneste parul',
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
                'description': 'Neutralizeaza reflexele galbene',
                'image': '../static/img/sampon4.jpg',
            },
            'product8': {
                'name': 'Sampon par vopsit',
                'price': 375,
                'quantity': '1000',
                'description': 'Hidratare, Protecția culorii',
                'image': '../static/img/sampon2.jpg',

            },
            'product9': {
                'name': 'Sampon pentru par gras',
                'price': 215,
                'quantity': '1000',
                'description': 'Curata eficient scalpul si parul',
                'image': '../static/img/sampon3.jpg',
            }
        }
        context['products'] = products
        return context



class BarbaTemplateView(TemplateView):
    template_name = 'shop/ingrijire_barba.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = {
            'product1': {
                'name': 'Balsam pentru barba',
                'price': 112,
                'quantity':60,
                'description': 'Se poate aplica pe barba umeda sau uscata',
                'image':'../static/img/barba1.jpg',
            },
            'product2': {
                'name': 'Ulei pentru barba si mustata',
                'price': 54,
                'quantity': '50',
                'description': 'Ulei cu efect hranitor pentru barba si mustata',
                'image': '../static/img/barba2.jpg',
            },
            'product3': {
                'name': 'Set cadou pentru barba',
                'price': 215,
                'quantity': '2 x75 ml',
                'description': 'Mentine barba sanatoasa si stralucitoare',
                'image': '../static/img/barba3.jpg',
            },

        }
        context['products'] = products
        return context
