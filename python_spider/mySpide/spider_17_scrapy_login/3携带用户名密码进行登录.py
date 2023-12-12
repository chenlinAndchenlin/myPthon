import requests


url = 'https://passport.17k.com/ck/user/login'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'Referer': 'https://passport.17k.com/login/',
}
data = {
    'loginName': '17346570232',
    'password': 'xlg17346570232'
}
session = requests.Session()
res = session.post(url, headers=headers, data=data)
print(res.content.decode())
url = 'https://user.17k.com/ck/user/myInfo/96139098?bindInfo=1&appKey=2406394919'
json = session.get(url).json()
print(json)

#     def start_requests(self):
#         # 登录的url地址
#         login_url = 'https://passport.17k.com/ck/user/login'
#         data = {
#             'loginName': '17346570232',
#             'password': 'xlg17346570232'
#         }
#         # data = 'loginName=17346570232&password=xlg17346570232'
#         # yield scrapy.Request(login_url, body=data, method='POST', callback=self.parse_do_login)
#         yield scrapy.FormRequest(login_url, formdata=data, callback=self.parse_do_login)
#
#     def parse_do_login(self, response, **kwargs):
#         # 当前对于start_urls中的地址进行请求
#         yield scrapy.Request(self.start_urls[0])
#
#     def parse(self, response, **kwargs):
#         print(response.text)