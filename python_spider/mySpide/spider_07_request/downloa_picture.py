import requests
url = 'https://ww4.sinaimg.cn/mw690/0076vsZ6ly1hiw5krf9wdj31401hcb2a.jpg'
response = requests.get(url)
with open("tupian.jpg","wb") as f:
    f.write(response.content)