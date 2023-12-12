import os.path
import time
from urllib.parse import urljoin
import requests
from lxml import etree
import random

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    }
shu={}
def jiexi_url_tree(url):
    response = requests.get(url, headers=headers)
    con = response.content.decode()
    tree = etree.HTML(con)
    return tree
def get_shu_url_book(sdmz_lianjie):
    for lianjie in sdmz_lianjie:
        url="https://www.shicimingju.com"+lianjie.xpath("./a/@href")[0]
        shuming=lianjie.xpath("./a/text()")[0]
        # print(url,shuming)
        shu[shuming]=url

def get_only_book_context(url):
    only_book_ml_html = jiexi_url_tree(url)
    ml_list = only_book_ml_html.xpath('//div[@class="book-mulu"]/ul/li')
    book={}
    for ml in ml_list:
        time.sleep(random.randint(1, 3))
        ml_title = ml.xpath('./a/text()')[0]
        # https://www.shicimingju.com/book/sanguoyanyi/1.html
        ml_con_url = "https://www.shicimingju.com" + ml.xpath('./a/@href')[0]
        ml_con_text_html = requests.get(ml_con_url, headers=headers)
        con = ml_con_text_html.content.decode()
        # print(con)
        cone = etree.HTML(con)
        ml_con_text_html_tree_con = cone.xpath('//div[@class="card bookmark-list"]//text()')
        book[ml_title]=ml_con_text_html_tree_con
    return book

def write_only_ml_context(book):

    if not os.path.exists("new_"+ListShu):
        os.mkdir("new_"+ListShu)
    for ml_title in book:

        with open(os.path.join("new_"+ListShu, ml_title + '.txt'), "w", encoding='UTF-8') as f:

            mu_con = ''.join(book[ml_title])

            f.write(mu_con)
        print("new_"+ListShu, "  ", ml_title, "  ", "downloa success！")


if __name__ == '__main__':
    起始_url="https://www.shicimingju.com/bookmark/sidamingzhu.html"
    # book_item_res=requests.get(起始_url,headers=headers)
    # sdmz_context_html=book_item_res.content.decode()
    # tree=etree.HTML(sdmz_context_html)
    tree_sibenshu_html=jiexi_url_tree(起始_url)
    sdmz_lianjie=tree_sibenshu_html.xpath('//div[@class="book-item"]/h3')
    # print(sdmz_lianjie)
    # https://www.shicimingju.com/book/sanguoyanyi.html
    # shu={}
    # for lianjie in sdmz_lianjie:
    #     url="https://www.shicimingju.com"+lianjie.xpath("./a/@href")[0]
    #     shuming=lianjie.xpath("./a/text()")[0]
    #     # print(url,shuming)
    #     shu[shuming]=url
    get_shu_url_book(sdmz_lianjie)
    # print(shu)
    for ListShu in shu:

        # print(shu[ListShu])
        # res_ml=requests.get(shu[ListShu],headers=headers)
        # res_ml=res_ml.content.decode()
        # tree=etree.HTML(res_ml)

        book=get_only_book_context(shu[ListShu])
        write_only_ml_context(book)
        # only_book_ml_html=jiexi_url_tree(shu[ListShu])
        # ml_list=only_book_ml_html.xpath('//div[@class="book-mulu"]/ul/li')
        # for ml  in ml_list:
        #     ml_title=ml.xpath('./a/text()')
        #     # https://www.shicimingju.com/book/sanguoyanyi/1.html
        #     ml_con_url="https://www.shicimingju.com"+ml.xpath('./a/@href')[0]
        #     ml_con_text_html = requests.get(ml_con_url, headers=headers)
        #     con=ml_con_text_html.content.decode()
        #     # print(con)
        #     cone=etree.HTML(con)
        #     ml_con_text_html_tree_con=cone.xpath('//div[@class="card bookmark-list"]//text()')
        #     # print(ml_con_text_html_tree_con)

            # if not os.path.exists(ListShu):
            #     os.mkdir(ListShu)
            # with open(os.path.join(ListShu,ml_title[0]+'.txt'),"w",encoding='UTF-8') as f:
            # # mu_con=''.join(ml_con_text_html_tree_con)
            # # print(mu_con)
            #     mu_con=''.join(ml_con_text_html_tree_con)
            #     # print(mu_con)
            #     f.write(mu_con)
            # print(ListShu,"  ",ml_title,"  ","downloa success！")
            # time.sleep(random.randint(1, 3))
        # print(len(ml_list))
        #     exit()
    # '//div[@class="book-mulu"]/ul/li'