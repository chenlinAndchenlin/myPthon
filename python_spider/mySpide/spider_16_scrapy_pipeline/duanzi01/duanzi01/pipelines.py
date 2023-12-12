# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql
from itemadapter import ItemAdapter


class Duanzi01Pipeline:
    # def process_item(self, item, spider):
    #     return item

    f = None

    def open_spider(self, spider):
        print('爬虫开始时被调用一次')
        print(spider.name)
        # 连接MySQL数据库
        self.db = pymysql.connect(host='127.0.0.1', user='root', password='root', db='python_test')
        # 设置字符编码
        self.db.set_charset('utf8')
        # 创建游标对象
        self.cursor = self.db.cursor()

        # self.f = open('./duanzi.text', 'w')

    # 爬虫文件中提取数据的方法每yield一次item，就会运行一次
    # 该方法为固定名称函数
    def process_item(self, item, spider):
        print("item:",item)
        title = item['title']
        con = item['con']
        try:
            sql = f'insert into dz(title, con) values("{title}", "{con}")'
            self.cursor.execute(sql)  # 执行SQL语句
            self.db.commit()  # 事务提交 写入到MySQL数据库中
        except Exception as e:
            print(sql, '===>', e)  # 打印错误异常信息
            self.db.rollback()  # 事务回滚
        # item是传递过来的数据
        return item

    def close_spider(self, spider):
        print('爬虫结束时被调用')
        self.db.close()
        self.cursor.close()
