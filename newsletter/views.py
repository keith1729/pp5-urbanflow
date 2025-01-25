from django.shortcuts import render, redirect
from .forms import SubscriberForm

# Create your views here.


def newsletter_signup(request):
    """ View to render sign up form """

    if request.method == 'POST':
        form = SubscriberForm(request.POST, user_email=request.user.email)
        if form.is_valid():
            form.save()
            return redirect('newsletter_thank_you')
    else:
        form = SubscriberForm(user_email=request.user.email)
    return render(request, 'newsletter_signup.html', {'form': form})

def newsletter_thank_you(request):
    """ View to render thank you message """

    return render(request, 'newsletter_thank_you.html')
