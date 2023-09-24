import scrapy


class ExpertzSpider(scrapy.Spider):
    name = 'expertz'
    allowed_domains = ['expertzlab.com']
    start_urls = ['http://expertzlab.com/']

    def parse(self, response):
        pass
