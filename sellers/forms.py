from django import forms
from . import models
from django.apps import apps
from django.contrib.auth import get_user_model
from prof.models import Code

class SellerForm(forms.ModelForm):
    class Meta:
        model = models.Seller
        fields = [
            'first_name',
            'last_name',
             'avatar',
             'street',
             'city',
             'state',
             'zipp',
             'display_name',
        ] 


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["avatar"].widget.attrs.update({'class': 'form-control'})
        self.fields["first_name"].widget.attrs.update({'class': 'form-control field', 'placeholder': 'First Name'})
        self.fields["last_name"].widget.attrs.update({'class': 'form-control', 'placeholder': 'Last Name'})
        self.fields["street"].widget.attrs.update({'class': 'form-control','placeholder': 'Street'})
        self.fields["city"].widget.attrs.update({'class': 'form-control', 'placeholder': 'City'})
        self.fields["state"].widget.attrs.update({'class': 'form-control', 'placeholder': 'State'})
        self.fields["zipp"].widget.attrs.update({'class': 'form-control', 'placeholder': 'Zip'})
        self.fields["display_name"].widget.attrs.update({'class': 'form-control', 'placeholder': 'Display Name'})

class PartialUserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = [

        ]


class CodeForm(forms.ModelForm):
    class Meta:
        model = Code
        fields = {
            
        }