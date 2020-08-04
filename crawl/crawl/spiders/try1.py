import scrapy
import re
from crawl.items import CrawlItem
from scrapy.selector import Selector
from scrapy.spiders import Spider, CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader.processors import Join, MapCompose, TakeFirst
from scrapy.pipelines.images import ImagesPipeline
from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging


class fileSpider(scrapy.Spider):
    name = 'crawlspider'
    custom_settings = {
        'DEPTH_LIMIT': 2,
        'ROBOTSTXT_OBEY': False
    }

    def __init__(self):
        self.start_urls = ["https://stackoverflow.com/questions?tab=Votes"]

    def parse(self, response):
        item = CrawlItem()
        for urls in response.xpath('//*[@class="question-summary"]/div[2]/h3/a/text()').extract():
            item['Title'] = urls
            yield item
        pass
