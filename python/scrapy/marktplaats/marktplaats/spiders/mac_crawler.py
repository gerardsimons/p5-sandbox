# -*- coding: utf-8 -*-
import scrapy


class MacCrawlerSpider(scrapy.Spider):
    name = "mac_crawler"
    allowed_domains = ["marktplaats.nl"]
    start_urls = (
        'http://www.marktplaats.nl/',
    )

    def parse(self, response):
        pass
