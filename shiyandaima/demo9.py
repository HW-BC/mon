#字符串
#字符串的驻留机制
a='hello'
b="hello"
c='''hello'''
print(a,id(a))
print(b,id(b))
print(c,id(c))#地址相同

#驻留，字符串只在编译时进行驻留，而非运行时
a="abc"
b="ab"+"c"
c="".join(["ab","c"])
print(a is b)
print(a is c)#is可以判断是否相等，严格相等id和值
print(id(a))
print(id(b))
print(id(c))#c的id与ab并不相同

#字符串的常用操作
s="hello，hello"
#正向索引
print(s.index("lo"))
print(s.find("lo"))#find优先用，元素找不到的时候不会抛出异常会返回-1
#以上查看lo出现的第一个位置
print(s.rindex("lo"))
print(s.rfind("lo"))#rfind优先用，元素找不到的时候不会抛出异常会返回-1
#以上查看lo出现的最后一个位置

#字符串的大小转化
s1="hello,python"
s2=s1.upper()#转成大写后，会产生一个新的对象
s3=s1.lower()#同样会产生一个新的对象
print(s1,id(s1))
print(s2,id(s2))
print(s3,id(s3))
print(s1==s3)#值相等
print(s1 is s3)#值和id均相等
s4="heLLO,world"
s5=s4.swapcase()
print(s5)#将字母大小写转化
s6=s4.title()
print(s6)#将每个单词的首字母大写

#字符串内容对齐
s1="hello,Python"
print(s1.center(20,"*"))#20指的是一共20个字，用center居中对齐，剩下的用*补充,如果不写就用 空格补充
print(s1.ljust(20,"*"))#左对齐
print(s1.rjust(20,"*"))#右对齐
print(s1.zfill(20))#右对齐，只指定长度，剩下的用0补充
print("-8910".zfill(8))#0加在了-右边

#字符串的劈分操作
s1="hello world python"
#split默认是从左开始分割
s2=s1.split()#默认以空格为分割
print(s2)
s3="hello|world|python"
print(s3.split(sep="|"))#指定劈分的字符串
print(s3.split(sep="|",maxsplit=1))#最大分1段
#rsplit()从右开始分割
print(s1.rsplit())
print(s3.rsplit("|"))#这里不需要写sep=
print(s3.rsplit(sep="|",maxsplit=1))

#
s="hello ,python"
print("1",s.isidentifier())#判断s是不是合法的标识符（只包含字母数字下划线 ）
print("2","heloo".isidentifier())
print("3","zhangsan_".isidentifier())
print("4","zhangsan_21".isidentifier())
print("5","\t".isspace())#是否全部由空白字符组成
print("6","abc".isalpha())#是否全部由字母组成
print("7","张三".isalpha())#单纯文字也算字母
print("8","张三1".isalpha())#1不是字符
print("9","123".isdecimal())#判断是否全部由十进制（阿拉伯）数字组成
print("10","123四".isdecimal())#四不是
print("11","123".isnumeric())#判断是否全部由数字组成
print("12","123四".isnumeric())#这里四就是数字，也包含I，II，
print("13","123abc".isalnum())#是否全部由字母和数字组成
print("14","123".isalnum())#范围会大
print("15","123abc!".isalnum())#有叹号就返回false

#字符串的替换replace（）
s="hello,python"
print(s.replace("python","java"))#用逗号后面的取代逗号前面的
s1="hello,python,python,python"
print(s1.replace("python","java",2))#换两次，2:最大替换次数
#字符串的合并join()
#列表的合并
lst=["hello","java","python"]
print(",".join(lst))#使用，逗号连接
#元组的合并
s=("hello","world","java")
print(",".join(s))
print("*".join("hello"))

#字符串的比较操作
print("apple" > "app")
print("apple" > "banana")#比较的是从一开始就比较如果向灯，则下一个直到不同，然后比较原始值
print(ord("a"),ord("b"))#这里明显看到a的原始值是97，b的原始值是98，所以b大于a
print(chr(97),chr(98))#这里输出的是97，98对应的字母
'''==与is的区别
==比较的是value
is比较的是id是否相等
'''
a=b="hello"
c="hello"
print(a==b)
print(a is b)
print(a==c)
print(a is c)

#字符串的的切片操作
s="hello,python"
s1=s[:5]#由于没有起始位置所以从0开始
s2=s[6:]#由于没有终止位置所以到结束截至
s3="!"
s4=s1+s3+s2
print(s4)#他们每一个新的字符串的id均不同
"""完整的写法"""
print(s[0:5:1])#相当于s[:5]。1：步长
print(s[::-1])#可以是负数相当于倒着切，默认从字符串结尾开始，开始结束
print(s[-6::1])

#格式化字符串:按照一定格式输出的字符串，相当于一个模板，填充部分
#第一种方式，使用%进行占位
name="张三"
age=20
print("我叫%s,今年%d岁" %(name,age))
#第二种方法：
print("我叫{0}，今年{1}岁".format(name,age))#0的是name，1的是age
#第三种方法
print(f"我叫{name},今年{age}岁")#前面要加上f
#表示精度和宽度
print("%10d"% 99)#10指的是宽度
print("%.2f"%3.1415926)#保留两位小数
#同时表示宽度和精度
print("%10.3f"%3.1415926)#总宽度为10，表六小数点后3位

print("{0}".format(3.1415926))#0索引,0可以不写
print("{0:.3}".format(3.1415926))#.3表示一共是三位数
print("{0:.3f}".format(3.1415926))#.3f表示小数点后三位数
print("{0:10.3f}".format(3.1415926))#宽度为10,小数点后两位

#字符串的编码转化
#编码过程
s="天涯共此时"
print(s.encode(encoding="GBK"))#在GBK这种编码中一个中文占两个字节
print(s.encode(encoding="UTF-8"))#在UTF这种编码中一个中文占三个字节
#解码操作
byte=s.encode(encoding="GBK")
print(byte.decode(encoding="GBK"))#byte代表就是一个二进制数据（字节类型的数据）
byte=s.encode(encoding="UTF-8")
print(byte.decode(encoding="UTF-8"))