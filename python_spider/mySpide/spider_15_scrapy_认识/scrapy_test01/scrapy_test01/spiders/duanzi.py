import scrapy

#spider
class DuanziSpider(scrapy.Spider):
    name = 'duanzi'
    allowed_domains = ['duanzixing.com']
    start_urls = ['http://duanzixing.com/']

    def parse(self, response,**kwargs):
        print(response)
