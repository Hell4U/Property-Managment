from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.translation import gettext as _

from .choices import states_choices, type_choices
from .forms import ListingForm
from .models import Listing


def listings(request):
    listings = Listing.objects.filter(is_published = True)
    paginator = Paginator(listings, 5)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    
    context = {'listings': paged_listings }

    return render(request, "listings/listings.html", context=context)

def listing(request,id):
    listing = get_object_or_404(Listing, id=id)
    context = {"listing":listing}
    return render(request, "listings/listing.html", context=context)

def search(request):
    listings = None
    if request.GET:
        listings = Listing.objects.filter(is_published = True)
        if "keywords" in request.GET:
            keywords = request.GET["keywords"]
            if keywords:
                listings= listings.filter(
                     Q(city__icontains=keywords)
                    | Q(state__icontains=keywords)
                    | Q(zipcode__icontains=keywords)
                )
        paginator = Paginator(listings, 6)
        page = request.GET.get("page")
        paged_listings = paginator.get_page(page)
        listings = paged_listings
    context = {
        "listings": listings,
        "values": request.GET,
    }

    return render(request, "listings/search.html", context=context)
    
@login_required
def upload(request):
    if request.method == "POST":
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            new_listing = form.save(commit=False)
            new_listing.user = request.user
            new_listing.save()
            messages.success(request, _("Uploaded successfully"))
            return redirect("listings")
        else:
            print(form.errors)
            messages.error(request, _("Information not valid"))
            return redirect("upload")
    else:
        form = ListingForm()

    context = {
        "state_choices": states_choices,
        "type_choices": type_choices,
        "form": form,
    }

    return render(request, "listings/upload.html", context)
