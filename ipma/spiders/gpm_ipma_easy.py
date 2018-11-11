# -*- coding: utf-8 -*-
from scrapy.spider import BaseSpider
from scrapy.linkextractors import LinkExtractor
from ipma.items import IpmaItem


class MySpider(BaseSpider):
    name = "ipma"
    allowed_domains = ["www.gpm-ipma.de"]
    start_urls = ["https://www.gpm-ipma.de/weiterbildung/projektmanager/aktuelle_lehrgangsangebote/detail/gpm_kombinationslehrgang_ipma_level_cb-81.html"]
    #start_urls = ["http://www.gpm-ipma.de/weiterbildung/"]


    def parse(self, response):
        a_selectors = response.xpath("//a")
        items = []
        for selector in a_selectors:
            item = IpmaItem()
            item ['page'] = response.url
            item ['text'] = selector.xpath("text()").extract_first()
            item ['link'] = selector.xpath("@href").extract_first()
            items.append(item)
        return items
