from django import forms
from .models import CustomerSubscriptionUser
from crispy_forms.helper import FormHelper


class CustomerSubscriptionForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control input-group mb-3','placeholder':'Enter First Name', 'style':'background-color: rgba(0, 0, 0, 0)' }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Last Name', 'style':'background-color: rgba(0, 0, 0, 0)'}))


    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Email', 'style':'background-color: rgba(0, 0, 0, 0)'}))

    class Meta:
        model = CustomerSubscriptionUser
        fields = ['first_name', 'last_name', 'email', ]

        def email_validation(self):
            email = self.cleaned_data.get('email')
            return email
        
        def first_name(self):
            email = self.cleaned_data.get('first_name')
            return first_name

        def last_name(self):
            email = self.cleaned_data.get('last_name')
            return last_name