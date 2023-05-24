

from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView

from cart.models import Cart


class HomeTemplateView(TemplateView):
    template_name = 'home/homepage.html'

