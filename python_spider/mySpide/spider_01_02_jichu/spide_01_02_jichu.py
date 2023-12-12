"""
字符
"""
# data="\t周润发\t \t chen\n"
# # 去除字符两边的空字符
# lst=data.strip()
# print(lst)
# print(data)
# data = "周润发\t \t \n马化腾\n \n樵夫"
# lst = data.split()
# print(lst)

# # 字符串格式
# name = "chenL"
# s = f"你好啊，{name}"
# s2=f"你好啊，{name}，{{LIN 林}}"
# print(s2)
# # 你好啊，chenL，{LIN 林}
#
# # # 一些老程序员喜欢这么干.
# s = "你好呀, 我叫{}, 今年{}岁".format(name, 18)
# s = "你好呀, 我叫%s, 今年%s岁" % (name, 18)
# print(s)

# 把字符串转化成字节
# bs = "我abc".encode("utf-8")
# bc = "我abc".encode("gbk")
# print(bs,len(bs))  #  b'\xe6\x88\x91\xe7\x9a\x84\xe5\xa4\xa9\xe5\x93\xaaabcdef'
# print(bc,len(bc))  #  b'\xe6\x88\x91\xe7\x9a\x84\xe5\xa4\xa9\xe5\x93\xaaabcdef'
# # 一个中文在utf-8里是3个字节. 一个英文是一个字节. 所以英文字母是正常显示的
# # 一个中文在gbk里是2个字节. 一个英文是一个字节. 所以英文字母是正常显示的
# # 输出
# # b'\xe6\x88\x91abc' 6
# # b'\xe6\x88\x91abc' 5
# # 把字节还原回字符串
# bs = b'\xe6\x88\x91\xe7\x9a\x84\xe5\xa4\xa9\xe5\x93\xaaabcdef'
# s = bs.decode("utf-8")
# print(s)

"""
文件操作
"""
# f = open("./葫芦娃.txt", mode="w", encoding="utf-8")
# f.write("哈哈哈")
# f.write("呵呵呵")  # 写完之后, 哈哈哈也会保留. 只有open的时候才会清空文件
# f.close()
# f = open("./葫芦娃.txt", mode="w", encoding="utf-8")
# f.write("哈哈哈1")
# f.write("呵呵呵1")  # 写完之后, 哈哈哈也会保留. 只有open的时候才会清空文件
# f.close()

"""
函数/模块
"""
# import random
# # 0.018783075814314154
# print(random.random())#0 1 之间的随机数
# print(random.randint(1, 5))  # [a, b]
# print(random.choice(["a", "b", "c"]))

# import datetime
# print(datetime.datetime.now())
# print(str(datetime.datetime.now()).split(".")[0])
# # 2023-11-17 16:56:00.108653
# # 2023-11-17 16:56:00
# import os
# file_path = "./hehe/haha/def.txt"
# # 得到一个路径的文件夹路径 得到一个最后的文件
# dir_name = os.path.dirname(file_path)
# base_name=os.path.basename(file_path)
# print(dir_name,base_name)
# # ./hehe/haha def.txt
#
# print(os.path.exists(dir_name))
# print(os.path.isdir(base_name))

"""
JSON
"""

def func(a, b):
    """
    樵夫设计的一个计算a+b的函数
    :param a:
    :param b:
    :return:
    """
    if type(a) != int or type(b) != int:
        # 主动抛出异常,一般在自己设计东西的时候能用到
        raise Exception("you should send me two number!!!!")
    return a + b


ret = func(1, "2")
print(ret)