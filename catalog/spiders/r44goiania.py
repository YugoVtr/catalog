import scrapy as spy
import re
from typing import Any, List

from scrapy.utils.response import open_in_browser
from scrapy.http.response.html import HtmlResponse
from scrapy.selector.unified import Selector

from catalog.items import CatalogItem


class R44GoianiaSpider(spy.Spider):
    name = "r44goiania"
    allowed_domains = ["www.44goiania.com"]
    start_urls = ["http://www.44goiania.com/"]

    def parse(self, response: HtmlResponse):
        links = response.xpath("//*/a/@href")
        links = set(filter(domain, links))

        for link in links:
            yield response.follow(url=link, callback=self.parse_categories)

    def parse_categories(self, response: HtmlResponse):
        body = re.search("<main(.|\n)+</main>", str(response.body.decode("utf-8")), flags=re.U)
        if body is None:
            return

        content = re.sub(" +", " ", body.group(0).replace("\n", " "))
        page = Selector(text=content)
        items = page.xpath('//*/div[@data-testid="gallery-item-panel"]')
        for item in items:
            titles = extract(item, '//*/div[@data-testid="gallery-item-title"]/text()')
            descriptions = extract(item, '//*/p[@data-testid="gallery-item-description"]/text()')

            if len(titles) != len(descriptions):
                self.logger.warning("wrong size")
                return

            for i in range(len(titles)):
                yield CatalogItem(
                    title=titles[i],
                    description=descriptions[i],
                    category=response.url.split("/")[-1],
                )


def domain(link: Selector) -> bool:
    return re.search("^https://www.44goiania.com/.+", link.get()) != None


def extract(i: Selector, m: str) -> List[str]:
    return i.xpath(m).getall()
