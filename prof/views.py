from django.shortcuts import get_object_or_404, render
from listings.models import Listing, Bought
from .models import Code
from django.http import HttpResponseRedirect, HttpResponse
from . import forms
from . import models

# Create your views here.
def bought_listings(request):
    uid = request.user.id
    boughts = Bought.objects.filter(buyer=request.user.id)
    
    return render(request, 'prof/bought_listings.html', {'boughts': boughts})


def redeem_detail(request, pk):
    bought = get_object_or_404(Bought, pk=pk)
    return render(request, 'prof/redeem_detail.html', {'bought': bought})

def redeem(request, pk):
    cd = get_object_or_404(Code, bought=pk)
    bought = get_object_or_404(Bought, pk=pk)
    #expire = now + datetime.timedelta(minutes = 10)

    form = forms.RedeemForm()
    form = forms.RedeemForm(request.POST)
    redeem = form['redeemed']
    r = form.save(commit=False)
    if redeem.value() == cd.code:
        bought.redeemed = True
        bought.save()
        return HttpResponseRedirect('/listings/home/')
    else:
        print(bought.id)
        print(cd.code)
        print("Not Correct code")
 
       

    return render(request, 'prof/redeem.html', {'form':form})