# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
import re

from pymongo import MongoClient

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

class PttPipeline:
    def __init__(self):
        self.ids_seen = set()

    def open_spider(self, spider):
        db_uri = spider.settings.get('MONGODB_URI', 'mongodb://localhost:27017')
        db_name = spider.settings.get('MONGODB_DB_NAME', 'gossip_scrapy')
        self.db_client = MongoClient('mongodb://localhost:27017')
        self.db = self.db_client[db_name]

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter['ID'] in self.ids_seen:
            raise DropItem(f"Duplicate item found: {item!r}")
        else:
            self.insert_article(item)
            self.ids_seen.add(adapter['ID'])
            return item

    def insert_article(self, item):
        item = dict(item)
        self.db.article.insert_one(item)

    def close_spider(self, spider):
        self.db_clients.close()
