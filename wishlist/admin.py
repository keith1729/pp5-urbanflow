from django.contrib import admin
from .models import Wishlist

# Register your models here.


class WishlistAdmin(admin.ModelAdmin): 

    list_display = (
        'user', 
        'product', 
        'created_at'
        )

    list_filter = ('created_at',) 
    search_fields = ('user__username', 'product__name')


admin.site.register(Wishlist, WishlistAdmin)