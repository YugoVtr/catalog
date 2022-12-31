import scrapy


class CatalogItem(scrapy.Item):
    title = scrapy.Field()
    description = scrapy.Field()
    category = scrapy.Field()
