# -*- coding: utf-8 -*-
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ipma.items import IpmaItem


class MySpider(CrawlSpider):
    name = "ipma"
    allowed_domains = ["www.gpm-ipma.de"]
    start_urls = ["https://www.gpm-ipma.de/weiterbildung/projektmanager/aktuelle_lehrgangsangebote/detail/"]
    #start_urls = ["http://www.gpm-ipma.de/weiterbildung/"]

    rules = [
        Rule(LinkExtractor(), callback="parse_items", follow=True),
    ]

    def parse_items(self, response):
        a_selectors = response.xpath("//a")
        items = []
        for selector in a_selectors:
            item = IpmaItem()
            item ['page'] = response.url
            item ['text'] = selector.xpath("text()").extract_first()
            item ['link'] = selector.xpath("@href").extract_first()
            items.append(item)
        return items
