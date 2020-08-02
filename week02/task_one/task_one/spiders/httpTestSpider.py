import scrapy


class HttpBinSpider(scrapy.Spider):
    name = 'httpIpTest'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/ip']

    def parse(self, response):
        print(response.text)
