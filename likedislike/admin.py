from django.contrib import admin
from .models import LikeDislike

# Register your models here.

 
class LikeDislikeAdmin(admin.ModelAdmin): 

    list_display = (
        'user', 
        'product', 
        'vote', 
        'created_at',
        ) 

    list_filter = ('vote', 'created_at') 
    search_fields = ('user__username', 'product__name')


admin.site.register(LikeDislike, LikeDislikeAdmin)