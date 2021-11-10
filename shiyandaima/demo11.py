#bug
#类型
age=int(input("请输入你的你年龄"))#input输入的时str类型
if age>=18:
    print("负责人")

#异常处理
#异常处理（try expect结构）
try:
    n1=int(input("输入第一个数："))
    n2=int(input("输入第二个数："))
    result=n1/n2
    print(result)
except ZeroDivisionError:#捕获除数为0的异常
    print("除数不准为0")
except ValueError:#捕获输入的时非数字串
    print("只能输入数字串")
except BaseException:#最大的错误（超父类）
    print("你就是错")
print("程序结束")

#异常处理（try except else  结构）
try:
    n1=int(input("输入第一个数："))
    n2=int(input("输入第二个数："))
    result = n1 / n2
except BaseException as e:#e是错误名称
    print("错误",e)
else :
    print(result)
print("程序结束")

#异常处理（try...except..else..finally结构）
try:
    n1=int(input("输入第一个数："))
    n2=int(input("输入第二个数："))
    result = n1 / n2
except BaseException as e:#e是错误名称
    print("错误",e)
else :
    print(result)
finally:
    print("无论是否产生异常，总会被执行的代码")
print("程序结束")

#数学运算的异常
#print(10/0)   ZeroDivisionError
#索引异常
lst=[11,22,33]
#print(lst[4])    IndexError索引只到3
#关键字异常
dic={"name":"zhangsan","age":20}
#print(dic["garden"])  KeyError dic中没有garden对应的value
#未声明初始化对象
#print(num)  NameError    num没有定义
#语法错误
#int a=20  SyntaxError python中不需要加上int
#传入无效的参数
#a=int("hello") ValueError

#异常处理的模块 打印出异常的信息
import traceback
try:
    print("________")
    print(10/0)
except:
    traceback.print_exc()

#使用raise Exception('分数不正确')进行手动抛出异常
try:
    score=int(input('请输入分数：'))
    if 0<=score<=100:
        print('分数为：',score)
    else:#手动抛出异常
        raise Exception('分数不正确')
except Exception as e:
    print(e)


def is_triangle(a,b,c):
    if a<0 or b<0 or c <0:
        raise Exception('三条边不能是负数')
    #判断是否构成三角形
    if a+b>c and b+c>a and a+c>b:
        print(f'三角形的边长a={a},b={b},c={c}')
    else:
        raise Exception(f'三角形的边长a={a},b={b},c={c},不能构成三角形')
if __name__ == '__main__':
    try:
        a=int(input('输入三角形一条边长：'))
        b=int(input('输入三角形一条边长：'))
        c=int(input('输入三角形一条边长：'))
        is_triangle(a, b, c)
    except Exception as c:
        print(c)

