# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

# scraper/scraper/items.py

import scrapy

class AirbnbListingItem(scrapy.Item):
    title = scrapy.Field()
    location = scrapy.Field()
    address = scrapy.Field()
    price_per_night = scrapy.Field()
    currency = scrapy.Field()
    total_price = scrapy.Field()
    image_urls = scrapy.Field()
    ratings = scrapy.Field()
    reviews = scrapy.Field()
    description = scrapy.Field()
    amenities = scrapy.Field()
    host = scrapy.Field()
    property_type = scrapy.Field()

    pass
