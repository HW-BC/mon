#range()的三种创建方式
'''第一种创建方式，只有一个参数（小括号种只给另一个数）'''
r=range(10)#[0,1,2,...,9]默认从0开始默认相差1称为步长
print(r)
print(list(r))#用于查看range对象中的整数序列 list：链表
'''第二种创建方式，给了两个参数（小括号中给了两个数）'''
r=range(1,10)#指定了起始值从一开始，到十结束但不包含十，默认步长为1
print(list(r))
'''第三种创建方式，给了三个参数'''
r=range(1,10,2)#指定起始值，终止值，步长
print(list(r))
'''判断指定的数值在序列中是否存在'''
print(10 in r)#返回false表示10不在r序列中
print(10 not in r)

'''循环结构'''
#while循环实例：
a=0
sum=0
while a<5:#注意冒号
    sum+=a
    a+=1
print(sum)
a=1
sum=0
while a<101:#注意冒号
    if a%2==0:#可以改进if not bool(a%2);加上bool时表示结果为true或者false不加上结果就是0或者非0，0对应的是false
        sum+=a
    a+=1
print('1到100之间的偶数和',sum)

#for循环：
for item in 'python':#依次取一个字母并执行print代码
    print(item)
#rangle（）产生一个整数序列，也是一个可迭代对象即能用for
for i in range(10):
    print(i)
#如果在循环体中不需要使用自定义变量，可将自定义变量写为"_"
for _ in range(5):#range(5)可以作为循环次数
    print("nt")
sum=0
for i in range(1,101):
    if i%2==0:
        sum+=i
print("1到100之间的偶数和为：",sum)
#实践
'''输出100到999之间的水仙花数'''
for item in range(100,1000):
    ge=item%10
    shi=item//10%10
    bai=item//100
    if item==ge**3+shi**3+bai**3:
        print(item)

#流程控制语句break
'''从键盘录入密码，最多只能循环三次'''
#正常写法：
for item in range(3):
    pwd=input("请输入密码")
    if pwd=='888':
        print("密码正确")
        break
    else:
        print("密码不正确")
a=3
while a>0:
    pwd=input("请输入密码")
    if pwd=='8888':
        print("腻害，密码正确")
        break
    else :
        a -= 1
        if a==0:
            print("憨批你没机会了")
        else:
            print("你还有" + str(a) + "次机会")
#continue语句
for item in range(1,51):
   if item%5==0:
        print(item)
for item in range(1,51):
    if item%5!=0:
        continue
    print(item)

#else语句
#else与for循环进行搭配
for item in range(3):
    pwd=input("请输入密码")
    if pwd=="8888":
        print("密码正确")
        break
    else:
        print("密码不正确")
else:
    print("三次均错")
#else与while循环进行搭配
a=0
while a<3:
    pwd=input("请输入密码")
    if pwd=="8888":
        print("密码正确")
        break
    else:
        print("密码不正确")
        a+=1
else :
    print("三次密码均输入错误")

#嵌套循环
# 输出三行四列的矩形
for i in range(1,4):#表示行数一次一行
    for j in range(1,5):
        print("*",end="\t")#目的是不让它换行
    print()#换行输出
#输出直角三角形
for i in range (1,10):
    j=1
    while j<=i:
        print("*",end="\t")
        j+=1
    print()
#输出九九乘法表
for i in range (1,10):
    for j in range(1,i+1):
        print(i,"*",j,"=",i*j,end="\t")
    print()

#嵌套循环中的break与continue循环
for i in range(5):
    for j in range(1,11):
        if j%2==0:
            continue
            #break
        print(j,end="\t")
    print()

