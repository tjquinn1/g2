from django.db import models
from django.forms import ModelForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone
from django.core.validators import RegexValidator


# Create your models here.
# Create the form class.
class Seller(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, null=True)
    avatar = models.FileField(upload_to='avatar/', null=True)
    created = models.DateTimeField(default=timezone.now)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=5, validators=[RegexValidator(r'^\d{1,10}$')])
    display_name = models.CharField(max_length=50, unique=True)
    

    
    
    UNITED_STATES = 'us'
    CANADA = 'ca'

    COUNTRY_CHOICES = (
        (UNITED_STATES, 'United State'),
        (CANADA, 'Canada',)
    )

    country = models.CharField(
        max_length = 2,
        choices = COUNTRY_CHOICES,
        default = UNITED_STATES,
    )

    def __str__(self):              # __unicode__ on Python 2
        return self.first_name