from django.views.generic import CreateView, ListView, TemplateView
from .models import Cart


class CartView(TemplateView):
    template_name = 'addcart/addcart.html'


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
