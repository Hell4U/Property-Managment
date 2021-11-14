from django import forms

from .models import Listing


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = (
            "title",
            "address",
            "address2",
            "city",
            "state",
            "zipcode",
            "price",
            "bedrooms",
            "bathrooms",
            "sqft",
            "type",
            "description",
            "feature_image",
            "image_1",
            "image_2",
            "image_3",
            "image_4",
        )
