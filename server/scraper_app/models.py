from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator

class Listing(models.Model):
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True, null=True)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    currency = models.CharField(max_length=10, default='USD')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    image_urls = models.JSONField(default=list, blank=True)  # list of image URLs
    ratings = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    number_reviews = models.IntegerField(blank=True, null=True)
    amenities = models.JSONField(default=list, blank=True)  # list of amenities
    host_info = models.JSONField(blank=True, null=True)  # JSON field for host details
    property_type = models.CharField(max_length=100, blank=True, null=True)
    scraped_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
