# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import Listing
from celery import shared_task
import celery

app = Celery('listings', broker='amqp://localhost')

@shared_task
def count():
    listings = Listing.objects.all()
    num = len(listings)
    return num
