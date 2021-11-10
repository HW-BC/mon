#列表
a=10
print(type(a))
lst=['hello','world',98]#列表的第一种创建方式
print(id(lst))
print(type(lst))
print(lst)
#第二种创建方式
lst2=list(['hello','world',98])
#列表的特点
lst=list(['hello','world',98,'hello'])#元素可重复
print(lst)
print(lst[0],lst[-4])#注意这里正向是从0开始，负向从-4开始

#链表索引
#利用index进行查找元素在列表中的位置
lst=["hello","world",98,"hello"]
print(lst.index("hello"))#如果列表中存在n个相同元素，只返回元素中的第一个元素的索引
#print(lst.index("dakwh"))
#print(lst.index("hello",1,3))#意思是在1到3之间查hello，但是数是从0开始的，不包含3，实际上查的是1，2
#获取列表中的单个元素
lst=["hello","world",98,"hello","world",234]
print(lst[2])
print(lst[-3])

#获取列表中的多个元素，采用切片
lst=[10,20,30,40,50,60,70,80]
#star=1,stop=6,step=1
#切片，格式：lst[star:stop:step]这其中区间是[star,stop)
#print(lst[1:6:1])
print("原列表",id(lst))
lst2=lst[1:6]
print("后列表",id(lst2))#表示切片前后的id不相同
#step那部分不写的话就默认为1，例：
print(lst[1:5])
#或者这样写：
print(lst[1:5:])
#stop部分不写默认为到末尾
print(lst[1::1])
#star部分不写默认为从0开始
print(lst[:5:1])
#step为负数的时候是逆序输出,在逆序输出的情况下，正常顺序定义起始和结尾
print(lst[::-1])
#都出现负数
print(lst[6::-1])
print(lst[-1::-1])

#列表元素的查询
print("p" in "python")
print("k" in "python")
lst=[10,20,30,40,"hello","world"]
print(10 in lst)
print(100 in lst)
print(100 not in lst)
#列表元素的遍历
for item in lst:
    print(item)

#向列表的末尾添加一个元素
lst=[10,20,30]
lst.append(100)
print(lst)#并不改变原来lst的id，知识在后面添加新元素
lst2=["hello","world"]
#向列表后面加上多个元素
lst.extend(lst2)
print(lst)
#向列表中指定位置插入元素
lst.insert(1,90)
print(lst)
#切片，在任意位置添加n多个元素,先切掉后面的一部分然后在补上心的
lst3=["憨","憨憨"]
lst[1:]=lst3
print(lst)

#列表元素的删除
lst=[10,20,30,10,100]
lst.remove(10)#移除列表中的10这个元素，如果有重复的则只移除第一次出现的
print(lst)
#lst.remove(1000)当要移除的对象不存在的时候，系统会报错
#pop根据索引移除元素,但是如果指定的索引不存在则抛出异常
lst.pop(1)
print(lst)
#如果不写索引，则默认列表中的最后一个元素
lst.pop()
print(lst)
#也可以使用切片
lst=[10,20,30,10,100]
#newlst=lst[1:3]#切片是产生了一个新的列表
#print("切片后的列表",newlst)
#不产生新切片对象的方法：
lst[1:3]=[]
print(lst)
#清楚列表中的所有元素
lst.clear()
print(lst)
#del语句将列表对象删除
del lst
print(lst)#结果报错，找不到这个列表

#列表元素的修改
lst=[10,20,30,40,50]
lst[2]=100
print(lst)
lst[1:3]=[200,300,400,500,600]#这里是先删除1，2再在1，2位置上增加元素，元素个数不限
print(lst)

#列表的排序操作
#sort()方法，将从小到大排序，可可以指定reserve=True，进行降序排序
lst=[50,20,90,80,23,100]
print(lst,id(lst))
lst.sort()#开始排序，调用对象的sort方法，默认升序排序,默认是lst.sort(reverse=False)
print(lst,id(lst))
#通过指定关键字参数，变成降序排序
lst.sort(reverse=True)
print(lst)
#使用内置函数sorted（）对列表进行排序，将产生一个新的列表
lst=[50,20,90,80,23,100]
print(lst)
newlst=sorted(lst)
print(newlst)
#指定关键字参数，实现降序排序
newlst2=sorted(lst,reverse=True)
print(newlst2)

#列表生成式，生成列表的公式
lst=[i*i for i in range(1,10)]#产生1到9的整数序列，第一个i是列表元素的表达式
print(lst)
lst=[i*2 for i in range(1,6)]
print(lst)#产生0到10的偶数
