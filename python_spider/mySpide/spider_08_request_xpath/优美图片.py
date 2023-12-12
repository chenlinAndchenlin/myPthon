import os
import random
import time

from lxml import etree
import requests
url = 'http://www.umeituku.com/bizhitupian/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}
res = requests.get(url, headers=headers)
data = res.content.decode()
tree = etree.HTML(data)
# 获取所有二级标签页的url地址
a_list = tree.xpath('//div[@class="TypeList"]/ul/li/a/@href')
path= 'img'
if not os.path.exists(path):
    os.mkdir(path)
for url in a_list:
    # 开始访问二级标签页内容
    res = requests.get(url, headers=headers)
    data = res.content.decode()
    tree = etree.HTML(data)
    try:
        # 找二级标签页当前大图的src地址和图片名称
        src = tree.xpath('//p[@align="center"]/a/img/@src')[0]
        alt = tree.xpath('//p[@align="center"]/a/img/@alt')[0]
        print(src, alt, '图片下载中======')
        # 图片存入本地
        with open(os.path.join(path, alt+'.jpg'), 'wb') as f:
            f.write(requests.get(src, headers=headers).content)
        print(src, alt, '图片下载完成......')
        # 给个时间自省
    except Exception as e:
        print(f'在抓取网址：{url}的过程中出现了问题， 问题为：', e)
    time.sleep(random.randint(1, 4))