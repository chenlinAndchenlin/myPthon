import requests

url = 'http://www.zishazx.com/product'
# 设置请求头
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}
# 鞋带的参数 get传参
params = {
    'page': 1,
    'size_id': 0,
    'volum_id': 0,
    'price_id': 2,
    'category_id': 1001,
    'prize_id': 0,
    'pug_id': 25
}

# 发起get请求  携带了 get传参 携带了headers请求头
response = requests.get(url, headers=headers, params=params)
# 获取返回数据
data = response.content.decode()
print(response.url)
# print(data)
# 写入
with open('zsh.html', 'w', encoding='UTF-8') as f:
    f.write(data)