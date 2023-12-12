import scrapy


class MzSpider(scrapy.Spider):
    name = 'mz'
    # allowed_domains = ['ezample.com']
    start_urls = ['https://www.shicimingju.com/bookmark/sidamingzhu.html']

    def parse(self, response, **kwargs):
        print(response.text)
