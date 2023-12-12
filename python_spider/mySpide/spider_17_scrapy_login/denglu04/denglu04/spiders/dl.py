import scrapy
import base64
import json
import requests
data = {
        "__VIEWSTATE": " BSJgtIbCzAde3JI9Qgy6V3vklArP+L32surmwDt98qq2TdTn4Q0OOn/ICwLzB/AyfNGfMmKQumYZWF5l4qDceXreg9L++PPk7M7WRgYQHrcSie8VgoETUseTcik+EoRpTi/+MXz/bm+za+5sM9lgd0XyWZg=",
        "__VIEWSTATEGENERATOR": "C93BE1AE",
        "from": "http://so.gushiwen.cn/user/collect.aspx",
        "email": "793390457@qq.com",
        "pwd": "xlg17346570232",
        # "code": "gsdf",
        "denglu": "登录",
    }
def base64_api(uname, pwd, img, typeid):
    with open(img, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        b64 = base64_data.decode()
    data = {"username": uname, "password": pwd, "typeid": typeid, "image": b64}
    result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        #！！！！！！！注意：返回 人工不足等 错误情况 请加逻辑处理防止脚本卡死 继续重新 识别
        return result["message"]
    return ""
class DlSpider(scrapy.Spider):
    name = 'dl'
    # allowed_domains = ['17k.com']
    yzm_url = ['https://so.gushiwen.cn/RandCode.ashx?t=1700455586806?']


    def start_requests(self):
        print("开始执行start_requests")

        # login_url = 'https://passport.17k.com/ck/user/login'
        # data = {
        #     'loginName': '17346570232',
        #     'password': 'xlg17346570232'
        # }
        # yield scrapy.FormRequest(login_url, formdata=data, callback=self.parse_doLogin)
        yield scrapy.Request(self.yzm_url[0],callback=self.parse_yzm)
    def parse_yzm(self,response,**kwargs):
        url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
        print("开始执行parse_yzm")
        with open("yzm.jpg", "wb") as f:
            f.write(response.body)
        img_path = "yzm.jpg"
        result = base64_api(uname='xiaolinlin', pwd='123410qaz', img=img_path, typeid=3)
        print(result)
        data['code'] = result
        yield scrapy.FormRequest(url, formdata=data)
        # yield scrapy.Request(url,body=data)
    # def parse_dl(self,response,**kwargs):
    #     with open('gsw.html', 'w', encoding='UTF-8') as f:
    #         f.write(res.content.decode())
    def parse(self, response,**kwargs):
        print("开始执行parse")
        with open('gsw.html', 'w', encoding='UTF-8') as f:
            f.write(response.text)