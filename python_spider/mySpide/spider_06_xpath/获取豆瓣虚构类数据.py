from lxml import etree

tree=etree.HTML(open("./素材/豆瓣.html", 'r', encoding='UTF-8').read())
li_list=tree.xpath("//ul[@class='cover-col-4 clearfix']/li")
for li in li_list:
    print(li)
    title=li.xpath("./div/h2/a/text()")
    print(title[0])