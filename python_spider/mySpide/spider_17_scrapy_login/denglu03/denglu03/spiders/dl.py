import scrapy


class DlSpider(scrapy.Spider):
    name = 'dl'
    # allowed_domains = ['17k.com']
    # url = 'https://user.17k.com/ck/user/myInfo/96139098?bindInfo=1&appKey=2406394919'
    start_urls = ['https://user.17k.com/ck/user/myInfo/102546849?bindInfo=1&appKey=2406394919']

    def start_requests(self):
        print("开始执行start_requests")

        login_url = 'https://passport.17k.com/ck/user/login'
        # data = {
        #     'loginName': '17346570232',
        #     'password': 'xlg17346570232'
        # }
        # yield scrapy.FormRequest(login_url, formdata=data, callback=self.parse_doLogin)

        data='loginName=17719895764&password=123410qwaszx'
        yield scrapy.Request(login_url, method="POST",body=data,callback=self.parse_doLogin)
    def parse(self, response,**kwargs):
        print("开始执行Parse")
        print("response.status:",response.status)
    def parse_doLogin(self, response,**kwargs):
        print("开始执行parse_doLogin")
        yield scrapy.Request(self.start_urls[0])
