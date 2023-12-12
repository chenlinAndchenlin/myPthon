import scrapy


class DzSpider(scrapy.Spider):
    name = 'dz'
    allowed_domains = ['duanzixing.com']
    start_urls = ['http://duanzixing.com/']

    def parse(self, response,**kwargs):
        article_list = response.xpath('//article[@class="excerpt"]')
        for article in article_list:
            title = article.xpath('./header/h2/a/text()').extract_first()
            con = article.xpath('./p[@class="note"]/text()').extract_first()
            data = {'title': title, 'con': con}
            # print(data)
            yield data