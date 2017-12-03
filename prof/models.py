from django.db import models
from django.forms import ModelForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone
from listings.models import Bought

class Code(models.Model):
    bought = models.ForeignKey(Bought, blank=False, null=False)
    code = models.CharField(max_length=10)
    created = models.DateTimeField(default=timezone.now)
    expire = models.DateTimeField()