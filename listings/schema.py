import graphene

from graphene_django.types import DjangoObjectType

from .models import Listing, Bought


class ListingType(DjangoObjectType):
    class Meta:
        model = Listing


class BoughtType(DjangoObjectType):
    class Meta:
        model = Bought


class Query(object):
    all_listings = graphene.List(ListingType)
    all_boughts = graphene.List(BoughtType)
    user_boughts = graphene.List(BoughtType)

    def resolve_all_listings(self, info, **kwargs):
        return Listing.objects.all()

    def resolve_all_boughts(self, info, **kwargs):
        # We can easily optimize query count in the resolve method
        return Bought.objects.all()
    
    def resolve_user_boughts( self, info, **kwargs):
        return Bought.objects.filter(seller_id=info.context.user)