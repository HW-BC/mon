from turtle import *
'''
#程序练习题2.1
TS=eval(input("请输入不带有符号的温度值："))
a=input("请输入温度的单位：")
if a in ['F','f']:
    C=(TS-32)/1.8
    print("转换后的温度是{}C".format(int(C)))
elif a in ['C','c']:
    F=int(1.8*TS+32)
    print("转换后的温度是{}F".format(F))
else:
    print("输入错误")

#程序练习题2.2
def money(number):
    if number[-1] in['$']:
        sum=eval(number[0:-1])*6
        print("转换后的人民币数值为：{}￥".format(sum))
    elif number[-1] in['￥']:
        sum = eval(number[0:-1]) / 6
        print("转换后的美元数值为：{}$".format(sum))
    else:
        print("输入错误")
number=input("请输入带有符号的金额（人民币用数字加￥，美元用数字加$）：")
money(number)

#程序练习题2.3
from turtle import *
setup(650,350,200,200)#设置显示窗口的长宽以及窗口与电脑屏幕左上边缘的距离
penup()#抬起画笔
fd(-250)#向当前行进方向前进distance距离
pendown()#落下画笔，这一行代码结合上面两行表示不绘制图线拿笔移动落笔
pensize(25)#设置画笔尺寸
#pencolor("purple")#设置画笔颜色，
colors = ["red","orange","yellow","green"]
seth(-40)#改变画笔绘制方向，设置接下来的移动方向，蛇往斜下方向移动
for i in range(4):
    color(colors[i])
    circle(40,80)#绘制一个弧形半径40，角度80
    circle(-40,80)
color("purple")#设置蛇的头部颜色，即转弯的部分
circle(40,40)#先转40°
fd(40)#前进40
circle(16,180)#再大转弯
fd(40*2/3)#再往前走

#程序练习题2.4
from turtle import *
setup(500,500)
fd(100)
seth(120)
fd(100)
seth(240)#seth函数的话是以当下的点做坐标系改变角度
fd(100)

#程序练习题2.5
from turtle import *
fd(100)
seth(-120)
fd(100)
seth(120)
fd(100)
seth(60)
fd(100)
seth(-60)
fd(200)
seth(-180)
fd(200)
seth(60)
fd(100)

#程序练习题2.6
setup(500,500)
for i in range(4):
    up()
    fd(20)
    pd()
    fd(160)
    up()
    fd(20)
    right(90)#顺时针旋转90°

#程序练习题2.7
up()
setpos(-150,20)#与goto命令一样，作用也是让画笔沿直线移动到坐标点(x,y)处
down()
left(30)#逆时针旋转30°
fd(100)
left(60)
for i in range(5):
    fd(100)
    right(120)
    fd(100)
    left(60)
fd(100)
right(120)
fd(100)
for n in range(6):
    fd(100)
    right(60)

#程序练习题2.8
left(90)
length=5
speed=20
for i in range(30):
    fd(length)
    left(90)
    fd(length)
    left(90)
    length+=5
    fd(length)
'''
