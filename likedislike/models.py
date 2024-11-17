from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class LikeDislike(models.Model): 
    """ Model to store likes and dislikes for products """

    LIKE = 1 
    DISLIKE = -1 
    VOTE_CHOICES = ( 
        (LIKE, 'Like'), 
        (DISLIKE, 'Dislike') 
        ) 
    
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE) 
    vote = models.SmallIntegerField(choices=VOTE_CHOICES) 
    created_at = models.DateTimeField(auto_now_add=True) 
    
    class Meta: 
        """ Meta class to define unique constraints for the LikeDislike model """
        unique_together = ('user', 'product', 'vote')
    
    class Meta:
        verbose_name_plural = 'Likes and Dislikes'