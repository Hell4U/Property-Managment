from django.shortcuts import render
from listings.choices import beds_min_choices, states_choices
from listings.models import Listing

# Create your views here.

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings':listings,
        'state_choices':states_choices,
        'beds_min_choices':beds_min_choices
    }
    return render(request,"pages/index.html",context)
