from django.shortcuts import render 
from products.models import Product 

def index(request): 
    """ View function for the home page of the site """

    products = Product.objects.all() 
    
    return render(request, 'home/index.html', {'products': products})

def custom_404(request, exception): 
    """ View for 404 error page """
    
    return render(request, '404.html', status=404)