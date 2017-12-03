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
from django.shortcuts import get_object_or_404, render
import random
import string
import datetime


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
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = forms.SellerForm(request.POST, request.FILES)
        signup = forms.PartialUserForm(instance=request.user, data=request.POST, files=request.FILES)
        # check whether it's valid:
        if form.is_valid():
            print("yes")
            # process the data in form.cleaned_data as required
            seller = form.save(commit=False)
            seller.user = request.user
            seller.save()
            sp = signup.save(commit=False)
            sp.is_seller = True
            sp.save()
            messages.add_message(request, messages.SUCCESS, "Listing added")
            # redirect to a new URL:
            return HttpResponseRedirect('/sellers/home/')
        else:
            print(form.is_valid())
            print(signup.is_valid())
            print(form.errors)
            print(signup.errors)

    return render(request, 'sellers/new.html', {'form': form, 'signup': signup})

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