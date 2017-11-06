from django import forms
from . import models
class ListingForm(forms.ModelForm):
    class Meta:
        model = models.Listing
        fields = [
            'name',
            'price',
             'desc',
             'unit',
             'document',
        ]

class BoughtForm(forms.ModelForm):
    class Meta:
        model = models.Bought
        fields = {
            
        }
        
