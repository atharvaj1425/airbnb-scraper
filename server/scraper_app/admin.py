# airbnb_scraper/scrapper_app/admin.py

from django.contrib import admin
from .models import Listing

admin.site.register(Listing)
