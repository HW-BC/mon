'''

#5.1更大田字格的输出
def tzg(n):
    hang=2*n+1
    for i in range(1,hang+1):
        if i%2==1:
            print(n*"+----",end="")
            print("+")
        else:
            print(n*"|    ",end="")
            print("|")
def main():
    n=int(input("请输入需要田字格的行数："))
    tzg(n)
main()

#5.2实现isOdd（）函数
def isOdd(n):
    try:
        m=int(n)
        if m%2==1:
            return True
        else:
            return False
    except ValueError:
        return "输入值不符合要求，要输入整数"
print(isOdd(input("请输入一个整数:")))

#5.3实现isNum（）函数
def isNum(n):
    try:
        n=eval(n)
        if type(n)==int or type(n)==float or type(n)==complex:
            print("True")
    except NameError:
        print("False")
def main():
    n=input("输入数据：")
    isNum(n)
main()

#5.4实现multi（）函数
def multi(str):
    try:
        sum=1
        for i in str.split():
            sum=sum*eval(i)
        return sum
    except:
        return "输入错误"
string=input("请输入要计算的参数，每个参数之间用空格隔开:")
print(multi(string))

#5.5实现isPrime函数
from math import sqrt
def isPrime(n):
        if n == 1:
            return False
        for i in range(2,int(sqrt(n))+1):#在一般领域，对正整数n，如果用2到根号n之间的所有整数去除，均无法整除，则n为质数。
            if n % i == 0:
                return False
        return True
try:
    n = eval(input("请输入要判断的数字:"))
    print(isPrime(n))
except:
    print("输入错误")

import turtle, datetime
def drawLine(draw):   #绘制单段数码管
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    turtle.right(90)
def drawDigit(digit): #根据数字绘制七段数码管
    drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,6,8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)
def drawDate(date):  #获得要输出的数字
    for i in date:
        drawDigit(eval(i))  #注意: 通过eval()函数将数字变为整数
def main():
    turtle.setup(800, 350, 200, 200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    drawDate(datetime.datetime.now().strftime('%Y%m%d'))
    turtle.hideturtle()
    turtle.exitonclick()#点击画布后消失
    #turtle.mainloop()和turtle.done()两种方法会使后面的代码无法运行
    #input()这玩意不好搞不要用第一个实在
main()

import turtle, datetime
def drawGap(): #绘制数码管间隔
    turtle.penup()
    turtle.fd(5)
def drawLine(draw):   #绘制单段数码管
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawGap()
    turtle.right(90)
def drawDigit(d): #根据数字绘制七段数码管
    drawLine(True) if d in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,6,8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if d in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if d in [0,1,2,3,4,7,8,9] else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)
def drawDate(date):
    turtle.pencolor("red")
    for i in date:
        if i == '-':
            turtle.write('年',font=("Arial", 18, "normal"))
            turtle.pencolor("green")
            turtle.fd(40)
        elif i == '=':
            turtle.write('月',font=("Arial", 18, "normal"))
            turtle.pencolor("blue")
            turtle.fd(40)
        elif i == '+':
            turtle.write('日',font=("Arial", 18, "normal"))
        else:
            drawDigit(eval(i))
def main():
    turtle.setup(800, 350, 200, 200)
    turtle.penup()
    turtle.fd(-350)
    turtle.pensize(5)
    drawDate(datetime.datetime.now().strftime('%Y-%m=%d+'))
    turtle.hideturtle()
    turtle.exitonclick()
main()
'''
