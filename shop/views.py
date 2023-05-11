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
                'image': '../static/img/sampon6.jpg',
            },
            'product3': {
                'name': 'Sampon pentru par gras',
                'price': 215,
                'quantity': '500',
                'description': 'Curata eficient scalpul',
                'image': '../static/img/sampon7.jpg',
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
                'image': '../static/img/sampon6.jpg',

            },
            'product9': {
                'name': 'Sampon pentru par gras',
                'price': 215,
                'quantity': '1000',
                'description': 'Curata eficient scalpul si parul',
                'image': '../static/img/sampon7.jpg',
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



class AccesoriiTemplateView(TemplateView):
    template_name = 'shop/accesorii.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = {
            'product1': {
                'name': 'Perie de par',
                'price': 83,
                'description': 'Perie de par cu peri de mistret si fire de nailon',
                'image':'../static/img/accesorii1.png',
            },
            'product2': {
                'name': 'Pieptene',
                'price': 54,
                'description': 'Permite crearea de coafuri texturizate/tapate',
                'image': '../static/img/accesorii2.png',
            },
            'product3': {
                'name': 'Perie rotativa',
                'price': 115,
                'description': 'Peria are un diametru de 63 mm,recomandat pentru par mediu si lung',
                'image': '../static/img/accesorii3.png',
            },
            'product4': {
                'name': 'Perie barba',
                'price': 45,
                'description': 'Realizata din lemn iar perii sunt o combinatie dintre un mixt sintetic si par de mistret',
                'image': '../static/img/accesorii4.png',
            },
            'product5': {
                'name': 'Foarfeca pentru barba si mustata',
                'price': 38,
                'description': 'Este foarte mica, usoara si foarte versatila, putand fi folosita pentru a retusa micile detalii',
                'image': '../static/img/accesorii5.png',
            },
            'product6': {
                'name': 'Aparat pentru tuns',
                'price': 421,
                'description': '30 de reglaje precise pentru lungimea de taiere, de la 0.5 la 15 mm; pana la 90 minute de utilizare',
                'image': '../static/img/accesorii6.png',
            },

        }
        context['products'] = products
        return context
