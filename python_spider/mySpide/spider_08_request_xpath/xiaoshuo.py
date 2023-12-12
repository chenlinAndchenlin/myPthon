import requests
from lxml import etree
url = 'https://www.readnovel.com/category'
# 给定请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}
# 发起请求
res = requests.get(url, headers=headers)
data = res.content.decode()
# print(data)
# 实例化tree对象
tree = etree.HTML(data)
li_list=tree.xpath("//div[@class='right-book-list']/ul/li")
print(li_list)
for li in li_list:
    # 获取封面
    img = li.xpath('./div[@class="book-img"]/a/img/@src')[0]
    # 获取标题
    title = li.xpath('./div[@class="book-info"]/h3/a/text()')[0]
    # 获取简介
    intro = li.xpath('.//p[@class="intro"]/text()')[0]
    print(img, title, intro)
