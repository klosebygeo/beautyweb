from django.shortcuts import redirect
from django.views.generic import CreateView, ListView

from shop.models import Product
from .models import Cart


class CartView(ListView):
    template_name = 'shop/cart_details.html'
    context_object_name = 'cart_items'

    def get_queryset(self):
        user_id = self.request.user.id
        reserved_products = Cart.objects.filter(id_user=user_id, status=False).values_list('id_produs',flat=True)
        details_for_products = Product.objects.filter(id__in=reserved_products)
        return details_for_products


def add_to_cart(request, id_p):
    user_id = request.user.id
    produs = Cart(id_user=user_id, id_produs=id_p)
    produs.save()
    return redirect(request.META['HTTP_REFERER'])


class RegisterProduct(CreateView):
    model = Cart
    template_name = 'addcart/addcart.html'
    fields = '__all__'  # sau specificați aici câmpurile dorite


class AllProducts(ListView):
    template_name = 'addcart/addcart.html'
    context_object_name = 'cart_items'

    def get_queryset(self):
        user_id = self.request.user.id
        return Cart.objects.filter(id_user=user_id, status=False)
