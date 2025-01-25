from django.contrib import admin
from .models import Subscriber

# Register your models here.


class SubscriberAdmin(admin.ModelAdmin):
    """ SubscriberAdmin model """

    list_display = ('email', 'date_subscribed')

admin.site.register(Subscriber, SubscriberAdmin)
