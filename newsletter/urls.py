from django.urls import path
from . import views


urlpatterns = [
    path('newsletter-signup/', views.newsletter_signup, name='newsletter_signup'),
    path('newsletter-thank-you/', views.newsletter_thank_you, name='newsletter_thank_you'),
]
