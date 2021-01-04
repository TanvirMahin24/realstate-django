from django.shortcuts import render
from .models import Listing

# Create your views here.


def index(request):
    listings = Listing.objects.all()
    context = {
        'listings': listings
    }
    return render(request, 'listings/listings.html', context)


def search(request):
    return render(request, 'listings/search.html')


def listing(request):
    return render(request, 'listings/listing.html')
