#函数:执行特定任务已完成特定的功能的代码
#函数的创建和调用
def calc(a,b):#a,b是形参，位置在函数的定义处
    c=a+b
    return c
result=calc(10,20)#10和20是实参
print(result)
result=calc(b=10,a=20)#此时对应传参，等号的左侧的变量的名称称为关键字参数，按照名字赋值
print(result)

#函数的参数传递
'''在函数调用过程中，进行参数的传递
如果是不可变对象，在函数体的袖中不会影响实参的值arg1的修改不会影响n1的值
如果是可变对象，在函数体内的修改会影响到实参的值，arg2的修改不会影响n2的值
'''
def fun(arg1,arg2):
    print("arge=",arg1)
    print("arg2=",arg2)
    arg1=100
    arg2.append(10)
    print("arg1=",arg1)
    print("arg2=",arg2)
    return
n1=11
n2=[10,20,30,40]
fun(n1,n2)#位置传参
print(n2)

#函数的返回值
#0的布尔值位false，非0的布尔值位true
def fun(num):
    oushu=[]
    jishu=[]
    for i in num:
        if i%2:
            jishu.append(i)
        else:
            oushu.append(i)
    return jishu,oushu
print(fun([10,29,34,23,44,53,55]))
'''
函数的返回值
（1）如果函数没有返回值{函数执行完毕后不需要给调用出提供数据} return可以省略不写
（2）函数的返回值如果是一个，直接返回原值
（3）函数的返回值如果是多个，返回的结果为元组
'''
def fun1():
    print("hello")#return 可以不写
fun1()
def fun2():
    return "world"
a=fun2()
print(a)
def fun3():
    return "hello","world"
print(fun3())
"""函数在定义是，是否需要返回值，视情况而定"""

#函数的参数定义
def fun(a,b=10):#如果只传一个参数，就直接给了a，传两个b被替代
    print(a,b)
fun(10)
fun(10,20)

#函数的参数定义
def fun(*a):#函数定义时的，可变的位置参数，函数不确定传的参的个数，结果是元组
    print(a)
    print(a[0])
fun(10)
fun(10,20)
fun(10,20,30)
#个数可变的关键字形参,结果是一个字典
def fun(**a):
    print(a)
fun(a=10)
fun(a=10,b=30,c=30)
'''
def fun(*a,*b):
    pass
    以上代码报错，因为可变的位置参数只能是一个
def fun(**a,**b):
    pass
    以上代码报错，因为可变的关键字参数只能是一个
'''
def fun(*a,**b):
    pass
'''
def fun(**a,*b):
    pass
程序报错
表示在一个函数的定义过程中，既有个数可变的关键字形参，也有个数可变的位置形参
要求个数可变的位置形参，放在个数可变的关键字形参之前
'''

def fun(a,b,c):#abc形参
    print("a=",a)
    print("b=",b)
    print("c=",c)
fun(10,20,30)
lst=[11,22,33]
fun(*lst)#在函数调用时，将列表中的每个元素都转化为位置实参传入
fun(a=100,c=200,b=300)#函数的调用，所以时关键字实参
dic={"a":111,"c":300,"b":200}#一一对应各找各的不按照顺序
fun(**dic)

def fun(a,b=10):#b实在函数的定义处，所以b是形参，而且进行了赋值，所以b为默认值形参
    print("a=",a)
    print("b=",b)
def fun2(*a):#个数可变的位置形参
    print(a)
def fun3(**a):#个数可变的关键字形参
    print(a)
def fun4(a,b,c,d):
    print("a=",a)
    print("b=",b)
    print("c=",c)
    print("d=",d)
fun2(10,20,30,40)
fun3(a=11,b=22,c=33)
#调用fun4函数
fun4(10,20,30,40)#位置实参传递
fun4(a=10,b=20,c=30,d=40)#关键字实参传递
fun4(10,20,c=30,d=40)#前两个位置实参传递，后两个关键字实参传递
'''需求：c，d只能采用关键字实参传递:修改成：'''
def fun5(a,b,*,c,d):#需要在ab与cd之间加上*，表示从这个*之后的参数只能使用关键字实参传递
    print("a=",a)
    print("b=",b)
    print("c=",c)
    print("d=",d)
fun5(a=10,b=20,c=30,d=40)#关键字实参传递
fun5(10,20,c=30,d=40)
'''函数定义时的形参的顺序问题'''
def fun(a,b,*,c,d,**e):
    pass#可以
def fun(*a,**b):
    pass#可以
def fun(a,b,*c,**d):
    pass#可以

#变量作用域问题
name=1#全局变量
print(name)
def fun():
    print(name)
fun()

def fun():
    global a#局部变量加上global后变成全局变量
    a=1
    print(a)
fun()
print(a)

#递归函数：if else语法
#6的阶乘
def fac(n):
    if n==1:
        return 1
    else:
        return n*fac(n-1)
print(fac(6))

#斐波那契函数
def fb(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fb(n-1)+fb(n-2)
print(fb(6))
for i in range(1,7):
    print(fb(i))#输出前斐波那契数列的前六项
