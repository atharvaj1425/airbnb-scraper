from django.urls import path
from .views import ListingListAPIView, add_listing

urlpatterns = [
    path('listings/', ListingListAPIView.as_view(), name='listings'),
    path('add_listing/', add_listing, name='add_listing'),
]
