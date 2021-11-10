#多分支条件语句
s=int(input("请输入你的成绩"))
if s>=90 and s<=100:
    print("A")
elif 80<=s<=89:#注意这里是elif，而且可以简化写法采用数学上的方式
    print("B")
elif s>=0 and s<=79:
    print("C")
else:
    print("输入错误")#最后一个依然是else

#嵌套if
answer=input("您是会员吗？y/n")
money=int(input("请输入购物金额"))
if answer=='y':
    print('尊贵的会员')
    if money>=200:
        print("打八折，付款金额为",money*0.8)
    elif money>100:
        print("打九折，付款金额为",money*0.9)
    else:
        print("原价付款金额为",money)
else:
    print("非会员")
    if money >= 200:
        print("打九五折，付款金额为", money * 0.95)
    elif money > 100:
        print("打九九折，付款金额为", money * 0.99)
    else:
        print("原价付款金额为", money)

'''条件表达式可以简化判断ab两值大小的代码
正常情况下，会if a>=b：输出a大于等于b
else 输出a小于b
'''
a=int(input("输入第一个数字"))
b=int(input("输入第一个数字"))
print(str(a)+"大于等于"+str(b) if a>b else str(a)+"小于"+str(b))
#条件判断如果为真则输出if前面的一部分，如果为假则输出if后面的一部分

#pass语句,什么都不做只是一个占位符，用到需要写语句的地方
#判断是否是会员
answer=input("您是会员吗？y/n")
if answer=='y':
    pass
else:
    pass

