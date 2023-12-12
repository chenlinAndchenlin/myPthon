import requests
from lxml import etree

# 要抓取的url
url = 'http://www.zishazx.com/product'
# 给请求头 ua
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}

res = requests.get(url, headers=headers)
# 获取响应的页面内容
data = res.content.decode()
# 实例化匹配对象
tree = etree.HTML(data)

li_list=tree.xpath('//ul[@class="list clearfix"]/li')
print(li_list)
for li in li_list:
    # 获取到图片的src地址
    img = li.xpath('./p[@class="img"]/a/img/@src')[0]
    name = li.xpath('./p[@class="name"]/text()')[0]
    p_no = li.xpath('./p[@class="p_no"]/text()')[0]
    print(img, name, p_no)