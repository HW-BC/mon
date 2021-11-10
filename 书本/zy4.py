'''
#4.1猜数游戏
from random import randint
num=randint(1,10)
times=0
while True:
    times+=1
    guess = int(input("请猜一个1到10的一个整数"))
    if guess>num:
        print("遗憾！太大了")
    elif guess<num:
        print("遗憾，太小了")
    elif guess==num:
        print("预测{}次，你猜中了！".format(times))
        break

#4.2统计不同字符个数
str=input("请输入一个字符串：")
english=0
num=0
kong=0
qita=0
for i in str:
    if i>='A' and i<='z':
        english+=1
    elif i>='0' and i<='9':
        num+=1
    elif i==" ":
        kong+=1
    else:
        qita+=1
print("输入的字符串中英文字符有{}个，数字有{}个，空格有{}个，其他字符有{}个".format(english,num,kong,qita))

#4.3最大公约数计算
num1=int(input("请输入第一个整数:"))
num2=int(input("请输入第二个整数:"))
num3=num1*num2
if num1<num2:
    num1,num2=num2,num1
while False==(num1 in [0,1]):
    num2,num1=num1,num2%num1
num3=num3/num2#最小公倍数=两数之积、最大公约数
print("最大公约数为：{}，最小公倍数为{}".format(num2,num3))

#4.4猜数游戏续
from random import randint
num=randint(0,100)
times=0
while True:
    times+=1
    guess = int(input("请猜一个1到100的一个整数"))
    if guess>num:
        print("遗憾！太大了")
    elif guess<num:
        print("遗憾，太小了")
    elif guess==num:
        print("预测{}次，你猜中了！".format(times))
        break

#4.5猜数游戏续
from random import randint
num=randint(0,100)
times=0
while True:
    times+=1
    try:
        guess = int(input("请猜一个1到100的一个整数"))
    except:
        print("输入内容必须为整数")
        break
    if guess>num:
        print("遗憾！太大了")
    elif guess<num:
        print("遗憾，太小了")
    elif guess==num:
        print("预测{}次，你猜中了！".format(times))
        break
'''
