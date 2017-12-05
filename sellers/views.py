from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from . import forms
from . import models
from listings.models import Listing
from accounts.models import User
from django.contrib.auth.decorators import login_required
from accounts.forms import UserCreateForm
from accounts.models import User
from listings.models import Bought
from sellers.models import Seller
from django.shortcuts import get_object_or_404, render
import random
import string
import datetime
import braintree


# Create your views here.
@login_required
def Home(request):
    user = request.user
    listings = Listing.objects.filter(user_id=request.user.id)
    return render(request, 'sellers/home.html', {'listings':listings}) 

@login_required
def New(request):
    form = forms.SellerForm()
    signup = forms.PartialUserForm(instance=request.user)
    # if this is a POST request we need to process the form data
    # create a form instance and populate it with data from the request)
    # check whether it's valid:
    if request.method == 'POST':
        form = forms.SellerForm(request.POST, request.FILES)
        signup = forms.PartialUserForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            seller = form.save(commit=False)
            seller.user = request.user
            seller.save()
            sp = signup.save(commit=False)
            sp.is_seller = True
            sp.save()
            return HttpResponseRedirect('/sellers/new2/')
        else:
            messages.add_message(request, messages.ERROR, "Error")
            print(form.errors)
            return HttpResponseRedirect('/sellers/new/')
    return render(request, 'sellers/new.html', {'form': form, 'signup':signup})

    

def TwoNew(request):
    seller = get_object_or_404(Seller, user=request.user)
    merch = forms.MerchForm()
    if request.method == 'POST':
        merch = forms.MerchForm(request.POST)
        terms = request.POST.get('tos')
        if terms == 'on':
            terms = True
        else:
            terms = False

        merchant_account_params = {
            'individual': {
                'first_name': seller.first_name,
                'last_name': seller.last_name,
                'email': seller.email,
                'phone': request.POST.get('phone'),
                'date_of_birth': request.POST.get('dob'),
                'ssn': request.POST.get('ssn'),
                'address': {
                    'street_address': seller.street,
                    'locality': seller.city,
                    'region': seller.state,
                    'postal_code': seller.zipp
                }
            },
            'business': {
                'legal_name': request.POST.get('legal'),
                'dba_name': request.POST.get('dba'),
                'tax_id': request.POST.get('tax'),
                'address': {
                    'street_address': request.POST.get('biz_street'),
                    'locality': request.POST.get('biz_city'),
                    'region': request.POST.get('biz_state'),
                    'postal_code': request.POST.get('biz_zipp')
                }
            },
            'funding': {
                'descriptor': request.POST.get('funding_name'),
                'destination': braintree.MerchantAccount.FundingDestination.Bank,
                'email': seller.email,
                'mobile_phone': request.POST.get('phone'),
                'account_number': request.POST.get('acc_num'),
                'routing_number': request.POST.get('routing'),
            },
            "tos_accepted": terms,
            "master_merchant_account_id": "BCSW"
        }




        result = braintree.MerchantAccount.create(merchant_account_params)
        form = forms.AddMerchForm(instance=seller)
        up = form.save(commit=False)
        up.merch = result.merchant_account.id
        up.save()
        return HttpResponseRedirect('/sellers/home/')
    return render(request, 'sellers/new2.html', {'merch':merch})

@login_required
def Profile(request):
    uid = request.user.id
    boughts = Bought.objects.filter(seller_id=uid)

    return render(request, 'sellers/profile.html', {'boughts': boughts})


def redeem(request, pk):
    
    bought = get_object_or_404(Bought, pk=pk)
    code = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(6))
    now = datetime.datetime.now()
    expire = now + datetime.timedelta(minutes = 10)

    form = forms.CodeForm()
    form = forms.CodeForm(request.POST)
    bought = get_object_or_404(Bought, pk=pk)
    c = form.save(commit=False)
    c.bought = Bought.objects.get(id = bought.id)
    c.code = code
    c.expire = expire
    c.save()

    return render(request, 'sellers/redeem.html', {'form':form, 'bought': bought, 'code': code})