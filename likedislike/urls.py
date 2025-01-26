from django.urls import path
from . import views

urlpatterns = [
    path(
        'product/<int:product_id>/like/',
        views.like_product,
        name='like_product'
    ),
    path(
        'product/<int:product_id>/dislike/',
        views.dislike_product,
        name='dislike_product'
    ),
]
