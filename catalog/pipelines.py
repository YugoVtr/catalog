from itemadapter import ItemAdapter
from catalog.items import CatalogItem


class CatalogPipeline:
    def process_item(self, item: CatalogItem, spider):
        return item
