from django.views.generic import CreateView, ListView
from .models import Cart

class RegisterProduct(CreateView):
    model = Cart
    template_name = 'addcart/addcart.html'

class AllProducts(ListView):
    template_name = 'addcart/addcart.html'

    def get_queryset(self):
        user_id = self.request.user.id
        return Cart.objects.filter(id_user=user_id, status=False)
