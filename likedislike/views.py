from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import LikeDislike
from products.models import Product

# Create your views here.


@login_required
def like_product(request, product_id):
    """ Handle the like action for a product """

    product = get_object_or_404(Product, id=product_id)
    like_dislike, created = LikeDislike.objects.get_or_create(
        user=request.user,
        product=product,
        vote=LikeDislike.LIKE
    )
    if not created:
        like_dislike.delete()

    return redirect('product_detail', product_id=product.id)


@login_required
def dislike_product(request, product_id):
    """ Handle the dislike action for a product """

    product = get_object_or_404(Product, id=product_id)
    like_dislike, created = LikeDislike.objects.get_or_create(
        user=request.user,
        product=product,
        vote=LikeDislike.DISLIKE
    )
    if not created:
        like_dislike.delete()

    return redirect('product_detail', product_id=product.id)
