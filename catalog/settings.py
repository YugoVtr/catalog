BOT_NAME = "catalog"

SPIDER_MODULES = ["catalog.spiders"]
NEWSPIDER_MODULE = "catalog.spiders"

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    "catalog.pipelines.CatalogPipeline": 300,
}

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
