from django.db import models
from django.forms import ModelForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone
from sellers.models import Seller

# Create your models here.
# Create the form class.
class Listing(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, null=True)
    document = models.FileField(upload_to='documents/', null=True)
    created = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    status = models.CharField(default="",null=True, blank=True, max_length=10)

    desc = models.TextField()
    
    HOUR = 'hr'
    SESSION = 'ss'

    UNIT_CHOICES = (
        (HOUR, 'Hour'),
        (SESSION, 'Session',)
    )

    unit = models.CharField(
        max_length = 2,
        choices = UNIT_CHOICES,
        default = HOUR,
    )

    def __str__(self):              # __unicode__ on Python 2
        return self.name


class Bought(models.Model):
    buyer = models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, null=True, related_name='buyers')
    seller = models.ForeignKey(Seller,null=True, blank=True)
    item = models.ForeignKey(Listing, blank=True, null=True, related_name='items')
    trans_id = models.CharField(default="",null=True, blank=True, max_length=8)
    created = models.DateTimeField(default=timezone.now)
    redeemed = models.BooleanField(default=False)