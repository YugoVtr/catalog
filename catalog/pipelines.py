import pymongo
from pymongo.errors import DuplicateKeyError

from itemadapter import ItemAdapter
from catalog.items import CatalogItem

import logging
class CatalogPipeline:

    collection_name = 'r44goiania'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item: CatalogItem, spider):
        try:
            self.db[self.collection_name].insert_one(ItemAdapter(item).asdict())
            return item
        except DuplicateKeyError as e:
            logging.info(f'DuplicateKeyError: {e.details}')
