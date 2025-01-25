from django.db import models

# Create your models here.


class Subscriber(models.Model):
    """ Recording newsletter subscribers data """

    email = models.EmailField(unique=True)
    date_subscribed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
