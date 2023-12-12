# 安装pymysql
# import pymysql
#
# db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root', database='python_test')
# print(db)
# # 没有-
# db.set_charset('utf8')
# cursor = db.cursor()
#
# sql = 'select * from student'
# cursor.execute(sql)
#
# print(cursor.fetchall())
# db.close()

# 安装pymysql
import pymysql

db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root', database='python_test')
# print(db)
# ((1, '陈', datetime.date(2012, 12, 23), '北京', '1234', '一年级1版'),
# (2, '李', datetime.date(2012, 12, 23), '北京', '1234', '一年级1版'))
# 没有-
db.set_charset('utf8')

cursor = db.cursor()
# 事务处理
try:
    # id为1的年龄改为20
    sql = 'update student set sname="王五" where sno=4'
    # sql = 'insert into student values(null, "陈lin", "2012-12-24", "北京", "12342775", "一年级1版")'
    cursor.execute(sql)
    # 受影响的行数
    print(cursor.rowcount)
    db.commit()  # 提交给数据库
except:
    print("数据修改失败！")
    db.rollback()  # 回滚到没有操作之前的状态
db.close()