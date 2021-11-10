'''字典，字典中是以一对一对存储的，以冒号分割,字典是无序的序列，第一个放在字典中的不一定在第一个位置'''
#放在字典中的序列必须是不可变序列（不可以执行增删改）
#字典的创建
#第一种
zidian={"张三":100,"李四":90,"王五":50}
print(zidian,type(zidian))
#第二种：
zi=dict(name="jack",age=20)
print(zi)
#创建空字典
d={}
print(d)

#字典元素的获取
zidian={"张三":100,"李四":90,"王五":50}
'''第一种方式使用[]'''
print(zidian["张三"])
'''第二种方法，使用get（）方法'''
print(zidian.get("张三"))
#区别：当[]要查找的东西的值不存在时【】会产生报错但，get方法会输出none
#print(zidian["陈"])#使用[]当不存在时会报错
print(zidian.get("chen"))#使用get（）方法不会报错，会输出none
print(zidian.get("chen",99))#99是当查找值不存在时，把99当成chen的值输出

#key字的判断
zidian={"张三":100,"李四":90,"王五":50}
print("张三" in zidian)
print("张三" not in zidian)
#字典元素的删除
del zidian["张三"]#删除指定的key-value对
print(zidian)
zidian.clear()#删除全部，清空字典的元素
print(zidian)
#字典元素的新增
zidian["陈留"]=98#添加key-value
print(zidian)
#修改指定的key的value
zidian['陈留']=100
print(zidian)

#获取字典视图的三个方法
zidian={"张三":100,"李四":90,"王五":50}
#获取所有的key
key=zidian.keys()
print(key,type(key))
print(list(key))#将所有组成的视图转成列表
#获取所有的value
value=zidian.values()
print(value,type(value))
print(list(value))
#获取所有的key-value
item=zidian.items()
print(item)
print(list(item))#使用list形成元组，[（）,()]

#字典元素的遍历
zidian={"张三":100,"李四":90,"王五":50}
for i in zidian:
    print(i,zidian[i],zidian.get(i))

#字典的key不可以重复，value可以重复
zidian={"xing":"zhang","xing":"wang"}#当重复时，会产生覆盖
print(zidian)
xm={"xing":"zhang","ming":"zhang"}#value可以重复
print(xm)
#字典时无序的不能指定位置添加元素
#字典中的key必须是不可变对象
lst=[10,20,30]
lst.insert(1,100)
print(lst)
#d={lst:100}    会报错因为key时lst，lst时可变对象
#print(d)

#字典生成式
key=["one","two","three"]
value=[1,2,3,4,6]#按照少的生成
zidian={keys.upper():values for keys,values in zip(key,value)}
print(zidian)#keys.upper()表示将字典中的所有key都变成大写的字母





