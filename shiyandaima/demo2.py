#输入input（）函数
word=input("你是谁？")
print("你的名字是："+word)#默认word是str类型
shu1=input("一个数")
shu2=input("另一个数")
#一种方法
print("两个数之和"+str(int(shu1)+int(shu2)))
#一种方法：
shu1=int(shu1)
shu2=int(shu2)
print("和是"+str(shu1+shu2))
#一种方法
shu3=int(input("一数"))
shu4=int(input("二数"))
print("两数和"+str(shu3+shu4))

#算术运算符
print(11/2)
print(11//2)#整除运算
print(11%2)
print(2**3)#幂运算，二的三次方
print(9//-4)#向下取整数原来应该是-2.25但向下取整就变成了-3
print(-9//4)
print(9%-4)#取余运算涉及到正负数时，这个用公式计算：余数=被除数-除数*商=9-（-4）*（-3）

#赋值运算符;从右向左运算
i=3+7
print(i)
#支持链式赋值
a=b=c=5
print(a,id(a))
print(b,id(b))
print(c,id(c))#数值地址相同，实际上只有一个整数对象，但有abc三个引用指向这个位置
#支持参数赋值
d=20
d+=20
print(d)
d/=3
print(d)#此时类型转化
d//=3
print(d)
d%=3
print(d)
#支持系列解包赋值
a,b,c,=10,20,30#顺序和等号左右的数量一定要对应
print(a,b,c)
#它好处是交换两个变量的值是不需要第三个变量
a,b=5,6
print("交换前",a,b)
a,b=b,a#实现两数值交换
print("交换后",a,b)

#比较运算符,比较运算符的返回值为布尔类型
a,b=10,20
print("a大于b吗？",a>b)
print("a大于等于b吗？",a>=b)
print("a等于b吗？",a==b)#==比较的是值而不是标识
print("a不等于b吗？",a!=b)

a=10
b=10
print(a==b)#true 说明他们的值相同
print(a is b)#true说明他们的标识即id（地址）相同，当给a赋值10时在给b赋值，b会先找有没有值相同的如果有则采用他的地址
lst1=[11,22,33,44]
lst2=[11,22,33,44]
print(lst1 == lst2)
print(lst1 is lst2)#(表明id不同)
print("a与b的id是不相同的",a is not b)
print("lst1与lst2的id是不相同的",lst1 is not  lst2)

#布尔运算符
a,b=1,2
#and运算符
print(a==1 and b==2)#true and true结果为true
print(a==1 and b<2)
print(a!=1 and b==2)
print(a!=1 and b!=2)#只要有一个为flase结果都为flase
#or运算符
print(a==1 or b<2)#只要有一个为true结果都为true
print(a!=1 or b!=2)
#not运算符
f=False
print(not f)
#in表示是在其中
s='hello world'
print('w' in s)
print('k' in s)
#not in表示不是在其中
print('w' not in s)
print('k' not in s)
#位运算符(将数据转成二进制进行计算)
print(4&8)#按位与&
print(4|8)
print(4<<1)#向左移动1位，相当于成2
print(4<<2)#向左移动2位相当于乘4
print(4>>1)#向右移动以为相当于除2

#判断布尔类型可用bool（）;以下值为False的情况，其他均为true
print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool(None))
print(bool(''))
print(bool(""))
print(bool([]))#空列表
print(bool(list()))#空列表
print(bool(()))#空元组
print(bool(tuple()))#空元组
print(bool({}))#空字典
print(bool(dict()))#空字典
print(bool(set()))#空集合