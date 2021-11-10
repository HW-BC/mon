#集合，集和是没有value的字典
#集合的创建
#第一种使用{}
s={1,2,3,4,5,6,4,2,3}
print(s)#结果是输出{1, 2, 3, 4, 5, 6}，可知集合是元素是不能重复的
#第二种创建方式使用内置函数set（）
s1=set(range(6))
print(s1,type(s1))
#将列表元素转化成集合
s2=set([1,2,3,4,5,6,8])
print(s2,type(s2))
#将元组元素转化成集和
s3=set((1,2,3,5,65,5))
print(s3,type(s3))#输出是{65, 1, 2, 3, 5} <class 'set'>，65在前面表示无序
#将字符串序列转化成集和
s4=set("python")
print(s4)
s5=set({4,5,3,4,6})
print(s5)
#空集合：
s6=set()
print(s6,type(s6))
s7={}
print(s7,type(s7))#这样定义的不是一个空集合，而是字典类型

#集合的相关操作
#集合元素的判断操作使用in或者not in
s={10,20,32,45,0}
print(10 in s)
print(100 in s)
print(10 not in s)
print(100 not in s)
#集和元素的增加
s.add(80)#一次只能添加一个元素
print(s)
s.update({200,300,400})#至少添加一个元素
print(s)
s.update([100,30])
s.update((78,98))
print(s)
#集合元素的删除元素
s.remove(32)
print(s)
#s.remove(66)使用remove时，所删除的元素必须要在原来集合中存在否则会报错
#print(s)
s.discard(500)
print(s)#与remove类似但是当原集和没有要删除的元素时，不会报错
s.pop()
print(s)#随意删除一个元素，不能指定删除的元素
s.clear()#删完
print(s)

#集和之间的关系
#判断两个集和是否相等
s1={10,20,30,40}
s2={40,30,20,10}
print(s1==s2)
print(s1!=s2)
#一个集合是否是另一个集合的子集
s1={30,40}
s2={10,20,30,40}
s3={10,20,50,60}
print(s1.issubset(s2))#s1是s2的子集
print(s2.issuperset(s1))#s2是s1的超集
print(s2.isdisjoint(s3))#s2和s3没有交集

#集合的数学操作
#交集操作
s1={10,20,30}
s2={20,30,40}
print(s1.intersection(s2))
print(s1 & s2)#q求交集
print(s1.union(s2))#求并集
print(s1 | s2)#并集操作
print(s1.difference(s2))#差集操作,属于s1不属于s2
print(s1-s2)#差集操作
#对称差集
print(s1.symmetric_difference(s2))#s1s2合集减去交集
print(s1^s2)

#集和生成式,生成集合的公式
#列表生成式：
lst=[ i*i for i in range(6)]
print(lst)
#集合生成式
s={i*i for i in range(10)}
print(s)
