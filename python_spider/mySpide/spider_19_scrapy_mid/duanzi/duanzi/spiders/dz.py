import scrapy


class DzSpider(scrapy.Spider):
    name = 'dz'
    # allowed_domains = ['duanzixing.com']
    start_urls = ['http://duanzixing.com/']

    def parse(self, response,**kwargs):
        print(response)
        # print(response.request.headers)
