# scraper/scraper/spiders/airbnb_spider.py

import scrapy
from scraper.items import AirbnbListingItem

class AirbnbSpider(scrapy.Spider):
    name = "airbnb_spider"
    allowed_domains = ["airbnb.com", "www.airbnb.co.in"]
    start_urls = ["https://www.airbnb.com/s/New-York--NY--United-States/homes"]


    def start_requests(self):
        # Construct the URL based on input parameters (hardcoded for demo)
        url = "https://www.airbnb.com/s/New-York--NY--United-States/homes"
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # Dummy data for demonstration; replace with real scraping logic
        item = AirbnbListingItem()
        item['title'] = "Cozy Apartment in NYC"
        item['location'] = "New York, USA"
        item['address'] = "123 Broadway, New York, NY"
        item['price_per_night'] = 120.00
        item['currency'] = "USD"
        item['total_price'] = 360.00
        item['image_urls'] = ["https://example.com/image1.jpg", "https://example.com/image2.jpg"]
        item['ratings'] = 4.8
        item['reviews'] = 150
        item['description'] = "A cozy apartment in the heart of NYC."
        item['amenities'] = ["WiFi", "Kitchen", "Air Conditioning"]
        item['host'] = {"name": "John Doe", "response_rate": "90%"}
        item['property_type'] = "Apartment"
        yield item

        # Optionally, handle pagination by following next page links
        # next_page = response.css('a.next::attr(href)').get()
        # if next_page:
        #     yield scrapy.Request(url=response.urljoin(next_page), callback=self.parse)
