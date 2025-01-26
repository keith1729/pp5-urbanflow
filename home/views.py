from django.shortcuts import render
from products.models import Product


def index(request):
    """ View function for the home page of the site """

    products = Product.objects.all()

    return render(request, 'home/index.html', {'products': products})
