
from datetime import datetime

import pytz
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Listing(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    sqft = models.IntegerField()
    type = models.CharField(max_length=20)
    feature_image = models.ImageField(upload_to="house/")
    image_1 = models.ImageField(upload_to="house/")
    image_2 = models.ImageField(upload_to="house/")
    image_3 = models.ImageField(upload_to="house/")
    image_4 = models.ImageField(upload_to="house/")
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now(pytz.timezone("Asia/Kolkata")))
  

    def __str__(self):
        return self.title
