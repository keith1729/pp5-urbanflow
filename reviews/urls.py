from django.urls import path 
from . import views 

urlpatterns = [ 
    path('product/<int:product_id>/add_review/', views.add_review, name='add_review'),  
    ]