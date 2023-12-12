# python操作MySQL数据库的类
import pymysql
class Test:
    db = ''
    cursor = ''
    # 链接数据库
    # def connect(self, host='127.0.0.1', port=3306, user='root', password='123456', database='test'):
    # 作为对象初始化（类一旦实例化 会自动执行）
    def __init__(self, host='127.0.0.1', port=3306, user='root', password='root', database='python_test'):
        self.db = pymysql.connect(host=host, port=port, user=user, password=password, database=database)
        self.db.set_charset('utf8')
        self.cursor = self.db.cursor()

    def select(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def inert_update_delete(self, sql):
        e = None
        try:
            self.cursor.execute(sql)
            self.db.commit()
            return self.cursor.rowcount
        except Exception as e:
            self.db.rollback()
            return e

    # 当程序执行完自动执行del方法
    def __del__(self):
        print('我是最后走的')
        self.db.close()

mysql = Test(host='localhost')
# mysql = Test()
# mysql.connect()
# print(mysql.db)
# print(mysql.__dict__)
# print(Test.__dict__)
print(mysql.select('select * from student'))