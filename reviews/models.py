from django.db import models
from django.contrib.auth.models import User 
from django.core.validators import MinValueValidator, MaxValueValidator
from products.models import Product

# Create your models here.

class Review(models.Model): 
    """ Model representing a product review """
    
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField() 
    date_added = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self): 
        return f"{self.user.username} - {self.product.name} - {self.rating}" 
        
    def save(self, *args, **kwargs): 
        super().save(*args, **kwargs) 
        self.update_product_rating() 
        
    def update_product_rating(self): 
        reviews = Review.objects.filter(product=self.product) 
        average_rating = reviews.aggregate(models.Avg('rating'))['rating__avg'] 
        self.product.rating = average_rating 
        self.product.save()