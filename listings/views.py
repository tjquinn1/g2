from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from . import forms
from . import models
from listings.models import Listing
from django.shortcuts import get_object_or_404, render
# Create your views here.

def Home(request):
    listings = Listing.objects.all()
    return render(request, 'listings/listing_home.html', {'listings':listings})

def New(request):
    form = forms.ListingForm()
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = forms.ListingForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            listing = form.save(commit=False)
            listing.user = request.user
            listing.save()
            messages.add_message(request, messages.SUCCESS, "Listing added")
            # redirect to a new URL:
            return HttpResponseRedirect('/listings/home/')

    return render(request, 'listings/new.html', {'form': form})

def detail(request, pk):
    listing = get_object_or_404(models.Listing, pk=pk)
    return render(request, 'listings/detail.html', {'listing': listing})

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
            messages.add_message(request, messages.SUCCESS, "Listing added")
            # redirect to a new URL:
            return HttpResponseRedirect('/listings/home/')

    return render(request, 'listings/bought.html', {'form': form, 'listing': listing})
    