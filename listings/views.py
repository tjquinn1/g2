from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from . import forms
from . import models
from listings.models import Listing
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

import braintree
# Create your views here.

def Home(request):
    listings = Listing.objects.filter(is_active=True)
    return render(request, 'listings/listing_home.html', {'listings':listings})

@login_required
def New(request):
    form = forms.ListingForm()
    # if this is a POST request we need to process the form data
    if request.user.is_seller == True:
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = forms.ListingForm(request.POST, request.FILES)
            # check whether it's valid:
            if form.is_valid():
                # process the data in form.cleaned_data as required
                listing = form.save(commit=False)
                listing.user = request.user
                listing.is_active = True
                listing.save()
                messages.add_message(request, messages.SUCCESS, "Listing added")
                # redirect to a new URL:
                return HttpResponseRedirect('/listings/home/')

        return render(request, 'listings/new.html', {'form': form})
    else:
        messages.add_message(request, messages.ERROR, "You have to sign up for a seller account before you can post a listing.")
        return HttpResponseRedirect('/sellers/new/')

def detail(request, pk):
    listing = get_object_or_404(models.Listing, pk=pk) 
    form = forms.DeleteForm(instance=listing)
    if request.method == 'POST':
        form = forms.DeleteForm(instance=listing, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save(commit=False)
            listing.is_active = False
            form.save()
            messages.success(request, "Listing Deleted")
            return HttpResponseRedirect('/sellers/home/')
    return render(request, 'listings/detail.html', {'listing': listing, 'form': form})

@login_required
def bought(request, pk):
    listing = get_object_or_404(models.Listing, pk=pk)
    form = forms.BoughtForm(instance=listing)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = forms.BoughtForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            bought = form.save(commit=False)
            bought.buyer = request.user
            bought.seller = listing.user_id
            bought.item = get_object_or_404(models.Listing, pk=pk)
            bought.save()
            messages.add_message(request, messages.SUCCESS, "Listing Purchased")
            # redirect to a new URL:
            return HttpResponseRedirect('/listings/home/')

    return render(request, 'listings/bought.html', {'form': form, 'listing': listing})


@login_required    
def Edit(request, pk):
    listing = get_object_or_404(models.Listing, pk=pk) 
    form = forms.ListingForm(instance=listing)
    
    if request.method == 'POST':
        form = forms.ListingForm(instance=listing, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Updated {}".format(form.cleaned_data['name']))
            return HttpResponseRedirect('/sellers/home/')
    return render(request, 'listings/edit.html', {'form': form})

def MyListings(request):
    uid = request.user.id
    listings = Listing.objects.filter(user_id=uid, is_active=True)
    return render(request, 'listings/my_listings.html', {'listings': listings})


def client_token(request):
  return braintree.ClientToken.generate()
@csrf_exempt
def new_checkout(request, pk):
    client_token = braintree.ClientToken.generate()
    listing = get_object_or_404(models.Listing, pk=pk)
    return render(request,'listings/new_checkout.html', {'client_token':client_token, 'listing':listing})

def show_checkout(request,transaction_id, pk):
    transaction = braintree.Transaction.find(transaction_id)
    result = {}
    TRANSACTION_SUCCESS_STATUSES = [
    braintree.Transaction.Status.Authorized,
    braintree.Transaction.Status.Authorizing,
    braintree.Transaction.Status.Settled,
    braintree.Transaction.Status.SettlementConfirmed,
    braintree.Transaction.Status.SettlementPending,
    braintree.Transaction.Status.Settling,
    braintree.Transaction.Status.SubmittedForSettlement
]

    if transaction.status in TRANSACTION_SUCCESS_STATUSES:
        if transaction.status == braintree.Transaction.Status.SubmittedForSettlement:
            listing = get_object_or_404(models.Listing, pk=pk) 
            form = forms.StatusForm()
            if request.method == 'POST':
                form = forms.StatusForm(request.POST)
                if form.is_valid():
                    form.save(commit=False)
                    listing.status = 'Authed'
                    form.save()
    if transaction.status in TRANSACTION_SUCCESS_STATUSES:
        result = {
            'header': 'Sweet Success!',
            'icon': 'success',
            'message': 'Your test transaction has been successfully processed. See the Braintree API response and try again.'
        }
    else:
        result = {
            'header': 'Transaction Failed',
            'icon': 'fail',
            'message': 'Your test transaction has a status of ' + transaction.status + '. See the Braintree API response and try again.'
        }

    return render(request,'listings/show_checkout.html', {'transaction':transaction, 'result':result, 'form':form})

def create_checkout(request, pk):
    listing = get_object_or_404(models.Listing, pk=pk)
    result = braintree.Transaction.sale({
        'amount': request.POST['amount'],
        'payment_method_nonce': request.POST['payment_method_nonce'],
        'options': {
            "submit_for_settlement": True
        }
    })

    if result.is_success or result.transaction:
        return HttpResponseRedirect('/listings/checkouts/{0}/{1}'.format(result.transaction.id, pk))
    else:
        #for x in result.errors.deep_errors: flash('Error: %s: %s' % (x.code, x.message))
        return HttpResponseRedirect('listings/checkouts/%i' % listing.id)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=True)