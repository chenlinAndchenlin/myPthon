import scrapy


class DlSpider(scrapy.Spider):
    name = 'dl'
    # allowed_domains = ['17k.com']
    start_urls = ['https://user.17k.com/ck/user/myInfo/102546849?bindInfo=1&appKey=2406394919']

    # 重写strat_requests
    def start_requests(self):
        cookie_str = 'GUID=5b7a7263-d2e8-404a-bb0a-5305fbe77a36; sajssdk_2015_cross_new_user=1; Hm_lvt_9793f42b498361373512340937deb2a0=1700444635; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F09%252F49%252F68%252F102546849.jpg-88x88%253Fv%253D1700444930556%26id%3D102546849%26nickname%3D%25E4%25B9%25A6%25E5%258F%258Bqj73t084m%26e%3D1715996930%26s%3D48de0be413dbe727; c_channel=0; c_csc=web; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22102546849%22%2C%22%24device_id%22%3A%2218bea65ff3f86e-01ac00097cef67-26031051-1327104-18bea65ff40fe1%22%2C%22props%22%3A%7B%7D%2C%22first_id%22%3A%225b7a7263-d2e8-404a-bb0a-5305fbe77a36%22%7D; Hm_lpvt_9793f42b498361373512340937deb2a0=1700445174'
        c_list = cookie_str.split("; ")
        print(c_list)
        cookie_dict = {}
        for cookie in c_list:
            list_cookie = cookie.split('=')
            cookie_dict[list_cookie[0]] = list_cookie[1]
        yield scrapy.Request(self.start_urls[0], cookies=cookie_dict)

    def parse(self, response, **kwargs):
        print(response.text)
