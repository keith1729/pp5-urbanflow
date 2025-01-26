from django import forms
from .models import Subscriber
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field


class SubscriberForm(forms.ModelForm):
    """ Subscriber form """

    class Meta:
        model = Subscriber
        fields = ['email']

    def __init__(self, *args, **kwargs):
        user_email = kwargs.pop('user_email', None)
        super().__init__(*args, **kwargs)
        if user_email:
            self.fields['email'].initial = user_email
            self.fields['email'].widget.attrs['readonly'] = True
            self.fields['email'].widget.attrs['class'] = (
                'form-control rounded-0'
            )
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('email', css_class='form-control rounded-0', readonly=True),
            Submit('submit', 'Sign Up')
        )
