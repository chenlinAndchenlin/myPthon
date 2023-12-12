import requests

url = 'http://www.baidu.com'

response=requests.get(url)

# print('response.status_code', response.status_code)
# print('response.url', response.url)
print('response.encoding', response.encoding)
print('response.text', response.text)

