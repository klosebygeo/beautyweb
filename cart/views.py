from django.db.models import Sum
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView
from shop.models import Product
from .models import Cart


def get_cart_details(request):
    template_name = 'shop/cart_details.html'
    context = {}
    user_id = request.user.id
    cart_items = Cart.objects.filter(id_user=user_id, status=False).all()
    context["cart_items"] = cart_items
    context["total"] = sum([item.quantity * item.produs.price for item in cart_items])
    return render(request, template_name, context)


def add_to_cart(request):
    user_id = request.user.id
    quantity = int(request.POST.get("quantity"))
    product_id = int(request.POST.get("product_id"))
    produs = Product.objects.filter(id=product_id).first()
    Cart.objects.create(id_user=user_id, produs=produs, quantity=quantity)
    quantity_of_products = Cart.objects.filter(id_user=user_id, status=0).aggregate(Sum('quantity'))
    response = {}
    response['count'] = quantity_of_products['quantity__sum']
    return JsonResponse(response)


class RegisterProduct(CreateView):
    model = Cart
    template_name = 'addcart/addcart.html'
    fields = '__all__'  # sau specificați aici câmpurile dorite


# conversie in functie cu http response
# class AllProducts(ListView):
#     template_name = 'addcart/addcart.html'
#     context_object_name = 'cart_items'
#
#     def get_queryset(self):
#         user_id = self.request.user.id
#         return Cart.objects.filter(id_user=user_id, status=False)

def all_products(request):
    template_name = 'addcart/addcart.html'
    context = {}
    user_id = request.user.id
    cart_items = Cart.objects.filter(id_user=user_id, status=False)
    context["cart_items"] = cart_items
    return render(request, template_name, context)


class ProductDeleteView(DeleteView):
    template_name = 'addcart/product_confirm_delete.html'
    model = Cart
    success_url = reverse_lazy('view-cart')


def allways_cart(request):
    response = {}
    response["count"] = 0
    if request.user.is_authenticated:
        user_id = request.user.id
        quantity_of_products = Cart.objects.filter(id_user=user_id, status=0).aggregate(Sum('quantity'))
        response['count'] = quantity_of_products['quantity__sum']
        return JsonResponse(response)
