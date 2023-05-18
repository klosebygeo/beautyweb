from django.views.generic import CreateView


# Create your views here.
class CartView(CreateView):
    template_name = 'addcart/addcart.html'

