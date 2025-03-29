from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Listing
from .serializers import ListingSerializer

# GET API: List all listings
class ListingListAPIView(generics.ListAPIView):
    queryset = Listing.objects.all().order_by('-scraped_at')
    serializer_class = ListingSerializer

# POST API: Add a new listing
@api_view(['POST'])
def add_listing(request):
    serializer = ListingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Listing added successfully', 'data': serializer.data}, status=201)
    return Response(serializer.errors, status=400)


# @api_view(['GET'])
# def get_listings(request):
#     listings = AirbnbListing.objects.all()
#     serializer = AirbnbListingSerializer(listings, many=True)
#     return Response(serializer.data)

# @api_view(['POST'])
# def add_listing(request):
#     serializer = AirbnbListingSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=201)
#     return Response(serializer.errors, status=400)
