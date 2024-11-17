from django.db import models
from likedislike.models import LikeDislike

# Create your models here.


class Category(models.Model):
    """ Model representing a product category """

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

    class Meta:
        verbose_name_plural = 'Categories'


class Product(models.Model):
    """ Model representing a product """

    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes_clothes = models.BooleanField(default=False, null=True, blank=True)
    has_sizes_shoes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def likes_count(self): 
        """ Count the number of likes for the product """
        return self.likedislike_set.filter(vote=LikeDislike.LIKE).count() 
    
    def dislikes_count(self): 
        """ Count the number of dislikes for the product """
        return self.likedislike_set.filter(vote=LikeDislike.DISLIKE).count()

    def __str__(self):
        return self.name

