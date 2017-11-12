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
             'is_active',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({'class': 'form-control', 'placeholder': 'Name'})
        self.fields["price"].widget.attrs.update({'class': 'form-control', 'placeholder': 'Price'})
        self.fields["desc"].widget.attrs.update({'class': 'form-control','placeholder': 'Description'})
        self.fields["unit"].widget.attrs.update({'class': 'form-control', 'placeholder': 'Per Hour or Session'})
        self.fields["document"].widget.attrs.update({'class': 'form-control'})
        self.fields["is_active"].widget.attrs.update({'class': 'form-control form-check-input'})
        

class BoughtForm(forms.ModelForm):
    class Meta:
        model = models.Bought
        fields = {
            
        }
        
class DeleteForm(forms.ModelForm):
    class Meta:
        model = models.Listing
        fields = {
            
        }

class StatusForm(forms.ModelForm):
    class Meta:
        model = models.Listing
        fields = {
            
        }