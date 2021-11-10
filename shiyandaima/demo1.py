print("hello\nworld")#换行
print("hello\tworld")
print("hell\tworld")
print("hellooo\tworld")#这里\t会以四个字符为一个组若在\t之前不够四个一组则补上剩下的，如果正好四个则再补四个
print("hello\rworld")#\r将hello覆盖掉
print("hello\bworld")#\b退回一个字符o
print("http:\\www.baidu.com")
print("http:\\\\www.baidu.com")#\相当于转义转成单纯字符形式而不是具有作用的字符
#print('老师说：'大家好'')不加\就会报错
print('老师说：\'大家好\'')
print("老师说：\"大家好\"")
print(r"hello\nworld")#不希望字符串中的转义字符起作用就要再“”前加上r或者R
#print(r"hello\nworld\")但是字符串后面不能加单独一个\
print(r"hello\nworld\\")#可以加两个\\

#print(chr(0b0100111001011000))#二进制所以在数字前要加上0b（这一串代表"乘"）
#print(ord('乘'))#打印出汉字“乘”对应的十进制
#import keyword
#print(keyword.kwlist)#以上两行代码是为了查看关键字
name='张旭鹤'
print('标识/地址/id',id(name))
print('类型',type(name))
print(name)

#不同进制问题
a=123
b=123.568
c=10101
print(a,type(a))
print(b,type(b))
print("十进制",a)
print("二进制",0b10101)#二进制以0b开头
print("八进制",0o176)#八进制以0o开头
print("十六进制",0xEAF)#十六进制以0x开头

#浮点数相加引用decimal包
#这个也不一定会出现结果不对，如果出现结果不对则可以用以下方法纠正
c=1.1
d=2.2
print(c+d)
from decimal import  Decimal
print(Decimal("1.1")+Decimal("2.2"))

#布尔类型,True与Flase可以直接转化为0和1，并且进行计算
e=True
f=False
print(e,type(e))
print(f,type(f))
print(e+f)

#字符串类型，不同“”的区别 单引号与双引号相同只能单行显示，三引号或三单号可以多行显示
str1='北陌，南笙'
str2="北陌，南笙"
str3='''北陌，南笙'''
str4='''北陌，
南笙'''
str5="""北陌，
南笙"""
print(str1)
print(str2)
print(str3)
print(str4)
print(str5)

#不同类型的值是不同一起输出的，但进行类型转化后就可以一起输出
name='张三'
age=15
#print(name+age)
print(name+str(age))
'''逗号，与加号+意思基本相同，但是如果使用加则前后的类型必须要一致'''

#注意在类型转化时str类型数字串为!!小数串!!是不能转,这个可以转成float类型
#sz='68.36'
#print(int(sz))！！！！！注意这样在print中转时并不改变原来的数据类型也就是此时68.36依然是str类型
#若想要改变数据类型则可以设一个新变量名并赋给他值：sz2=float(sz)
