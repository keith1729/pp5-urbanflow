from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Wishlist
from products.models import Product

# Create your views here.


@login_required
def wishlist(request):
    """ View a users wishlist items """

    wishlist_items = Wishlist.objects.filter(user=request.user)

    return render(
        request,
        'wishlist/wishlist.html',
        {'wishlist_items': wishlist_items}
    )


@login_required
def add_to_wishlist(request, product_id):
    """ Add a product to the user's wishlist """

    product = get_object_or_404(Product, id=product_id)
    Wishlist.objects.get_or_create(user=request.user, product=product)

    return redirect('product_detail', product_id=product.id)


@login_required
def remove_from_wishlist(request, product_id):
    """ Remove a product from the user's wishlist """

    product = get_object_or_404(Product, id=product_id)
    wishlist_item = get_object_or_404(
        Wishlist,
        user=request.user,
        product=product
    )
    wishlist_item.delete()

    return redirect('product_detail', product_id=product.id)
