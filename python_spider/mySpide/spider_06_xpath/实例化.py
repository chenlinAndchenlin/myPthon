from lxml import etree
data = open('./素材/豆瓣.html', 'r', encoding='UTF-8').read()
# 将新的html源代码解析为对象
tree = etree.HTML(data)
print(tree)