from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Listing

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True).all()
    paginator = Paginator(listings, 6)
    page = request.GET('page')
    paged_listings = paginator.get_page(page)

    context = {
        "listings": paged_listings
    }
    return render(request, 'listings/listings.html', context)

def listing(request):
    return render(request, 'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html')