#面向对象
#类的创建
class Student:#Student为类名，类名：由一个或多个单词组成，每个字母的首字母大写，其余小写
    native_place="河南"#直接写在类里面的变量成为类属性
    def __init__(self,name,age):
        self.name=name#self.name称为实例属性，进行了赋值操作，将局部变量name赋给实例属性
        self.age=age
    #实例方法：
    def eat(self):
        print("学生在吃饭")
    #在类之外定义的成为函数，在类之内定义的叫方法
    #静态方法：
    @staticmethod
    def methon():#()里面不能写self
        print("我使用了staticmethon进行修饰，所以我是静态方法")
    #类方法：
    @classmethod
    def cm(cls):
        print("类方法，使用了classmethon修饰")
#创建student的对象
stu=Student("张三",20)#因为上面的init里面有两个参数所以传两个参数
stu.eat()#1.对象名。方法名   调用Student类的eat方法
#另一种调用方法：
Student.eat(stu)#2.类名。方法名（类的对象：方法定义处的self）
print(stu.name)
print(stu.age)
#类属性的使用方式
print(Student.native_place)
stu1=Student("张三",20)
stu2=Student("李四",30)
print(stu1.native_place)
print(stu2.native_place)
Student.native_place="北京"#整体修改则所有的对象对应的值都会修改
print(stu1.native_place)
print(stu2.native_place)
stu2.native_place="中国"#仅仅是一个对象改变只会修改该对象的值，不会修改类中的值
print(Student.native_place)
print(stu1.native_place)
print(stu2.native_place)
#类方法:
Student.cm()#类方法的调用
#静态方法：
Student.methon()#静态方法的调用

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age#self.name和self.age是所有对象所共有的
    def eat(self):
        print(self.name+"在吃饭")
stu1=Student("张三",15)
stu2=Student("李四",16)
print("------为stu2动态绑定性别属性-------")
stu1.sex="女"#单独指定stu1添加这个性别属性,只为stu1单独绑定性别属性
print(stu1.name,stu1.age,stu1.sex)
print(stu2.name,stu2.age)
#动态绑定的方法
stu1.eat()
stu2.eat()#正常，定义在类方法中的
#定义在类之外的方法
def show():
    print("定义在类之外的，称为函数")
stu1.show=show#给stu1动态绑定show方法
stu1.show()
#stu2.show()会报错，因为没有给sth2绑定show方法，

class Car:#类是对属性和方法的封装
    def __init__(self,brand):
        self.brand=brand
    def start(self):
        print("汽车已启动")
car=Car("宝马")
car.start()
print(car.brand)

#封装
class Student:
    def __init__(self,name,age):
        self.name=name
        self.__age=age#年龄不希望在类的外部被使用，所以加了两个下划线————
    def show(self):
        print(self.name,self.__age)
stu=Student("张安",20)
stu.show()
#在类的外部调用姓名和年龄
print(stu.name)
#print(stu.__age)报错，age是内部变量
#print(dir(stu))#内置函数dir（）可以查看指定对象的所有属性
print(stu._Student__age)#在类的外部可以通过_Student__age进行访问,不建议访问

#继承
#单继承
class Person(object):#person继承object类
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(self.name,self.age)
class Student(Person):
    def __init__(self,name,age,no):
        super().__init__(name,age)
        self.no=no
    def info(self):#方法重写
        super().info()#调用父类的info方法
        print(self.no)#输出学号
class Teacher(Person):
    def __init__(self,name,age,year):
        super().__init__(name,age)
        self.year=year
    def info(self):
        super().info()
        print(self.year)
stu=Student("张三",20,"2020")
tea=Teacher("李四",30,"2005")
stu.info()
tea.info()

#多继承，C同时继承A，B类
class A(object):
    pass
class B(object):
    pass
class C(A,B):
    pass

#方法重写
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):#重写str，此时str不在输出内存地址，而是作为一个函数，实现其功能
        return "我的名字是{0}，今年{1}岁".format(self.name,self.age)
stu=Student("张三",15)
print(dir(stu))
print(stu)#默认会调用__str__（）方法

#多态
class Animal(object):
    def eat(self):
        print("动物会吃")
class Dog(Animal):
    def eat(self):
        print("狗吃骨头")
class Cat(Animal):
    def eat(self):
        print("猫吃鱼")
class Person(object):
    def eat(self):
        print("人吃五谷杂粮")
def fun(obj):
    obj.eat()
fun(Cat())
fun(Dog())
fun(Animal())
print("----------------")
fun(Person())#不需关心person的父类是谁，只需要他由eat方法，
'''静态语言必须要指明父类是谁，动态语言只需要有方法'''

#特殊方法和特殊属性
class A:
    pass
class B:
    pass
class C(A,B):
    def __init__(self,name,age):
        self.name=name
        self.age=age
#创建c类对象
x=C("jack",20)#x是c类对象的实例对象
print(x.__dict__)#查看实例对象属性的字典
print(C.__dict__)#查看的是类对象的属性和方法的字典
print(x.__class__)#输出对象所属的类
print(C.__bases__)#输出了C类父类类型的元素，放到了一个元组中
print(C.__base__)#输出第一个父类类型的元素
print(C.__mro__)#查看类的层次结构
print(A.__subclasses__())#查看所有子类（A的子类有c）

#特殊方法
a=20
b=100
c=a+b
d=a.__add__(b)#相当于c=a+b
print(c)
print(d)
class Student:
    def __init__(self,name):
        self.name=name
    def __add__(self, other):
        return self.name+other.name#添加一个add方法实现加法运算
    def __len__(self):
        return len(self.name)#添加一个ken方法实现计算name的长度
stu1=Student("张三")
stu2=Student("李四")
s=stu1+stu2#在Student中编写了add这个特殊的方法，所以可以相加
s=stu1.__add__(stu2)#另一种方法相当于上一行的代码
print(s)
lst=[11,22,33,44]
print(len(lst))
print(lst.__len__())#和上一行代码作用相同
print(len(stu1))#当在Student类中增加了len方法就可以使用这种方式知道长度

class Person(object):
    def __new__(cls, *args, **kwargs):
        print("__new__被调用执行，cls的id值为{0}".format(id(cls)))
        obj=super().__new__(cls)
        print("创建的对象的id为：{0}".format(id(obj)))
        return obj
    def __init__(self,name,age):
        print("__init__方法被调用，self的id值为{0}".format(id(self)))
        self.name=name
        self.age=age
print("object这个类对象的id为{0}".format(id(object)))
print("Person这个类对象的id为{0}".format(id(Person)))
#创建Person类的实例对象
p=Person("张三",20)
print("p这个Person类的对象的id为{0}".format(id(p)))

#类的浅拷贝与深拷贝
#变量的赋值操作
class CPU:
    pass
class Disk:
    pass
class Computer:
    def __init__(self,cpu,disk):
        self.cpu=cpu
        self.disk=disk
#变量的赋值：只是形成两个变量，实际上还是指向同一个对象
cpu1=CPU()
cpu2=cpu1
print(cpu1)
print(cpu2)
#类的浅拷贝
disk=Disk()#创建一个硬盘类的对象
computer=Computer(cpu1,disk)#创建一个计算机类的对象
#浅拷贝
import copy#引入copy包
print(disk)
computer2=copy.copy(computer)
print(computer,computer.cpu,computer,disk)
print(computer2,computer2.cpu,computer2,disk)
#深拷贝
computer3=copy.deepcopy(computer)
print(computer,computer.cpu,computer.disk)
print(computer3,computer3.cpu,computer3.disk)
'''深拷贝连对象的子类也会copy创建一个新的'''






