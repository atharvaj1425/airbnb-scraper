# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# scraper/scraper/pipelines.py

import json
import requests

class AirbnbScraperPipeline:
    def process_item(self, item, spider):
        # Convert lists to JSON strings if necessary
        if isinstance(item.get('amenities'), list):
            item['amenities'] = json.dumps(item['amenities'])
        if isinstance(item.get('image_urls'), list):
            item['image_urls'] = json.dumps(item['image_urls'])
        # Post the item to the Django backend
        url = "http://127.0.0.1:8000/api/add_listing/"
        headers = {"Content-Type": "application/json"}
        data = dict(item)
        response = requests.post(url, json=data, headers=headers)
        if response.status_code != 201:
            spider.logger.error(f"Failed to post item: {response.text}")
        return item

