from django.views.generic import CreateView, ListView
from .models import Cart


# Create your views here.

class RegisterProduct(CreateView):
    model = Cart
    template_name = 'addcart/addcart.html'


class AllProducts(ListView):  # se foloseste si pentru toate produsele neachitate si pt
    # produse dintr-un anumit cart
    template_name = 'addcart/addcart.html'

    def get_queryset(self):
        return Cart.objects.filter(id_user=user_id, status=0)
