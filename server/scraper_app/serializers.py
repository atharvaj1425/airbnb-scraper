# # airbnb_scraper/scrapper_app/serializers.py

# from rest_framework import serializers
# from .models import Listing
# import json

# class ListingSerializer(serializers.ModelSerializer):
#     amenities = serializers.SerializerMethodField()
#     image_urls = serializers.SerializerMethodField()

#     class Meta:
#         model = Listing
#         fields = '__all__'

#     def get_amenities(self, obj):
#         try:
#             return json.loads(obj.amenities) if obj.amenities else []
#         except Exception:
#             return []

#     def get_image_urls(self, obj):
#         try:
#             return json.loads(obj.image_urls) if obj.image_urls else []
#         except Exception:
#             return []

# airbnb_scraper/scrapper_app/serializers.py

import json
from rest_framework import serializers
from .models import Listing

class ListingSerializer(serializers.ModelSerializer):
    # Use JSONField to allow writing lists/dicts directly
    amenities = serializers.JSONField()
    image_urls = serializers.JSONField()

    class Meta:
        model = Listing
        fields = '__all__'

    def create(self, validated_data):
        # Convert amenities and image_urls to JSON strings for storage
        if 'amenities' in validated_data and isinstance(validated_data['amenities'], list):
            validated_data['amenities'] = json.dumps(validated_data['amenities'])
        if 'image_urls' in validated_data and isinstance(validated_data['image_urls'], list):
            validated_data['image_urls'] = json.dumps(validated_data['image_urls'])
        return super().create(validated_data)

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        # Convert stored JSON strings back to lists for output
        if ret.get('amenities'):
            try:
                ret['amenities'] = json.loads(ret['amenities'])
            except Exception:
                ret['amenities'] = []
        if ret.get('image_urls'):
            try:
                ret['image_urls'] = json.loads(ret['image_urls'])
            except Exception:
                ret['image_urls'] = []
        return ret
