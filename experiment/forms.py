from django import forms
from .models import CustomerSubscriptionUser
from crispy_forms.helper import FormHelper


class CustomerSubscriptionForm(forms.ModelForm):
    class Meta:
        model = CustomerSubscriptionUser
        fields = ['email']

        def email_validation(self):
            email = self.cleaned_data.get('email')
            return email