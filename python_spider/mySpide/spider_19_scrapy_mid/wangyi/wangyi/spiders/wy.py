import scrapy


class WySpider(scrapy.Spider):
    name = 'wy'
    # allowed_domains = ['https://news.163.com/']
    start_urls = ['https://news.163.com/']
    li_index = [1, 2]  # 当前要爬取菜单的索引位置
    page_url = []
    def parse(self, response,**kwargs):
       menu= response.xpath('//div[@class="ns_area list"]/ul/li/a/@href').extract()
       # print(menu)
       for i in range(len(menu)):
           if i in self.li_index:
               url = menu[i]
               # print(url)
               self.page_url.append(url)
               # 向详情页发起请求
               yield scrapy.Request(url, callback=self.parse_detail)

    def parse_detail(self, response,**kwargs):
        #  page_url=response.xpath('//div[@class="ndi_main"]/div/div/div/div/h3/a/@href').extract()
        page_detail_url = response.xpath('//div[@class="ndi_main"]/div/a/@href').extract()
        # page_url=response.xpath('//div[@class="ndi_main"]/div/a/@href').extract()
        print(page_detail_url)
        for url in page_detail_url:
            print(url)
            yield scrapy.Request(url, callback=self.parse_detail_con)

    def parse_detail_con(self, response,**kwargs):
        con=response.xpath('//div[@class="post_main"]//text()').extract()
        title=response.xpath('//h1[@class="post_title"]/text()').extract_first()
        data={"title":title,"con":con}
        print(data)


