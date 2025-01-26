from django.urls import path
from . import views

urlpatterns = [
    path('wishlist/', views.wishlist, name='wishlist'),
    path(
        'product/<int:product_id>/add_to_wishlist/',
        views.add_to_wishlist,
        name='add_to_wishlist'
    ),
    path(
        'product/<int:product_id>/remove_from_wishlist/',
        views.remove_from_wishlist,
        name='remove_from_wishlist'
    ),
    ]
