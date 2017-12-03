from django import forms
from django.forms import ModelForm, TextInput
from . import models
from django.apps import apps
from listings.models import Bought




class RedeemForm(forms.ModelForm):
    class Meta:
        model = Bought
        fields = {
            'redeemed',
        }

        widgets = {
            'redeemed': TextInput(attrs={'cols': 80, 'rows': 20}),
        }