from django import forms
from .models import Subscriber
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class SubscriberForm(forms.ModelForm):
    """ Subscriber form """

    class Meta:
        model = Subscriber
        fields = ['email']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Sign Up'))
