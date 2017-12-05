from django import forms
from . import models
from django.apps import apps
from django.contrib.auth import get_user_model
from prof.models import Code
from sellers.models import Seller

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
             'email',
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
        self.fields["email"].widget.attrs.update({'class': 'form-control', 'placeholder': 'Email'})
        
        

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

class MerchForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=100)
    phone = forms.CharField(max_length=10)
    dob = forms.CharField(max_length=10)
    ssn = forms.CharField(max_length=10)
    legal = forms.CharField(max_length=100)
    dba = forms.CharField(max_length=100)
    tax = forms.CharField(max_length=100)
    biz_street = forms.CharField(max_length=100)
    biz_state = forms.CharField(max_length=100)
    biz_city = forms.CharField(max_length=100)
    biz_zipp = forms.CharField(max_length=100)
    funding_name = forms.CharField(max_length=100)
    acc_num = forms.CharField(max_length=100)
    routing = forms.CharField(max_length=100)
    tos = forms.BooleanField()




    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.update({'class': 'form-control field', 'placeholder': 'First Name'})
        self.fields["phone"].widget.attrs.update({'class': 'form-control field', 'placeholder': 'Phone'})
        self.fields["dob"].widget.attrs.update({'class': 'form-control field', 'placeholder': 'DOB'})
        self.fields["ssn"].widget.attrs.update({'class': 'form-control field', 'placeholder': 'SSN'})
        self.fields["legal"].widget.attrs.update({'class': 'form-control field', 'placeholder': 'Legal Name'})
        self.fields["dba"].widget.attrs.update({'class': 'form-control field', 'placeholder': 'DBA'})
        self.fields["tax"].widget.attrs.update({'class': 'form-control field', 'placeholder': 'Tax Id'})
        self.fields["biz_street"].widget.attrs.update({'class': 'form-control field', 'placeholder': 'street'})
        self.fields["biz_city"].widget.attrs.update({'class': 'form-control field', 'placeholder': 'city'})
        self.fields["biz_state"].widget.attrs.update({'class': 'form-control field', 'placeholder': 'state'})
        self.fields["biz_zipp"].widget.attrs.update({'class': 'form-control field', 'placeholder': 'biz_zipp'})
        self.fields["funding_name"].widget.attrs.update({'class': 'form-control field', 'placeholder': 'Bank Account Name'})
        self.fields["acc_num"].widget.attrs.update({'class': 'form-control field', 'placeholder': 'Account Number'})
        self.fields["routing"].widget.attrs.update({'class': 'form-control field', 'placeholder': 'Routing Number'})
        self.fields["tos"].widget.attrs.update({'class': 'form-control field'})


class AddMerchForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = [
            'merch'
        ]