#模块
#一个模块可以包含函数，包含类，包含语句
def fun():
    pass
class Sudent:
    native_place = "河南"  # 直接写在类里面的变量成为类属性
    def __init__(self, name, age):
        self.name = name  # self.name称为实例属性，进行了赋值操作，将局部变量name赋给实例属性
        self.age = age
    # 实例方法：
    def eat(self):
        print("学生在吃饭")
    # 静态方法：
    @staticmethod
    def methon():  # ()里面不能写self
        print("我使用了staticmethon进行修饰，所以我是静态方法")
    # 类方法：
    @classmethod
    def cm(cls):
        print("类方法，使用了classmethon修饰")
a=1
b=2
c=a+b

#导包的第一种方式，导入math的所有
import math#导入math包，关于数学运算的模块
print(id(math),type(math),math)
print(math.pi)
print(dir(math))
print(math.pow(2,3),type(math.pow(2,3)))#2的三次方
print(math.ceil(9.001))#最接近的最大整数
print(math.floor(9.9999))#最接近的最小整数
#导包的第二种方式，导入的包中的特定方法
from math import pi#只导入了pi
print(pi)#直接使用pi，不需要用math。pi

def add(a,b):#当别人调用这个时整个程序就会运行一遍所以为了不运行下面那个print语句
    return a+b
if __name__ == '__main__':#当你只有单独运行demo14时这个print才会执行
    print(add(10, 20))

#导入包的注意事项
#使用import方式导入时，只能跟包名或者模块名
import 暑假
import demo1
#使用from..import可以导入包，模块，函数，变量等
from 暑假 import demo1
from 暑假.demo1 import a

#python中常用的内置模块
#sys与Python解释器及其环境操作相关的标准库
import sys
print(sys.getsizeof(24))#获取字节大小
print(sys.getsizeof("jahwgdk"))
import time#提供与时间相关的各种函数的标准库
print(time.time())#秒
print(time.localtime(time.time()))
#import urllib.request用于读取来自网上(服务器）的数据标准库
#print(urllib.request.urlopen("http://www.baidu.com").read())


