'''
#3.1重量计算
weight=float(input("请输入你现在的体重(kg)"))
earthweight=weight+0.5*10
moonweight=(weight+0.5*10)*0.165
print("10年后你在地球的体重是:{:.3f},在月球的体重是:{:.3f}".format(earthweight,moonweight))

#3.2天天向上续
import math
dayup=1
for i in range(1,365):
    if i%7 in [1,2,3]:
       dayup=dayup
    else:
        dayup=dayup*(1+0.01)
print("365天后能力值是{:.2f}".format(dayup))

dayup = 1
dayfactor = 0.01
for j in range (1,366):
    if j%7 in [4,5,6,0]:
        dayup = dayup *(1 + dayfactor)
print ( '%f the result is %.2f'%(dayfactor, dayup))

#3.3天天向上续
dayup=1
decrease=0
for i in range(1,366):
    temp=i-decrease
    tom=temp%7
    if i%10==0:
        decrease+=i-(tom-1)
        tom=1
    if tom in [4, 5, 6, 0]:#不用原始的天数进行判断因为10天一更新，引用一个新的变量待替天数
        dayup = dayup * (1 + 0.01)
print("365天后能力值是{:.2f}".format(dayup))

#回文数判断
hws=input("请输入一个五位数字：")
if len(hws)==5:
    a=hws[4:]+hws[3:4]+hws[2:3]+hws[1:2]+hws[0:1]
    if eval(hws)==eval(a):
        print("这是一个回文数")
    else:
        print("这不是一个回文数")
else:
    print("输入错误")

#3.5田字格的输出
for i in range(11):
    if i in [0,5,10]:
        print("+ - - - - + - - - - +")
    else:
        print("|         |         |")
'''
from time import sleep
print("Starting",end="")
for i in range(10):
    print("..",end="")
    sleep(0.5)
print("Done!")