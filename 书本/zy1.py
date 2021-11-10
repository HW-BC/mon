#1.1 字符串连接
str1=input("请输入你的名字：")
str2=input("请输入一个形容你的词：")
print(str1+"真"+str2)
print("{}真{}".format(str1,str2))

#1.2  1到N即加法
'''
n=input("请输入整数N：")
sum=0
for i in range(int(n)):
    sum+=i+1
print("1到N的求和是",sum)
'''

#1.3九九乘法表
'''
for i in range(1,10):
    for j in range(1,i+1):
        print("{}*{}={:2}".format(i,j,i*j),end=" ")#:2是保留两位
    print("")
'''

#1.4计算阶乘相加
'''
sum,tem=0,1
for i in range(1,11):
    tem*=i
    sum+=tem
print("运算结果是：{}".format(sum))
'''

#1.7五角星的绘制
'''
from turtle import *
color('red','yellow')
begin_fill()
while True:
    forward(200)
    right(144)
    if abs(pos())<1:
        break
end_fill()
'''