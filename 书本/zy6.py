"""
#随机密码生成
from random import randint
def random():
    mm=''
    for i in range(8):
        j=randint(0,62)
        if j>=10:
            if 90<(j+55)<97:
                mm+=chr(j+62)
            else:
                mm+=chr(j+55)
        else:
            mm+='%d'%j
    return mm
def main():
    for i in range(1,11):
        print("生成的第{}个密码是：{}".format(i,random()))
main()

#重复元素判定
def main():
    num=[]
    n=input("请输入一个元素")
    while n!="":
        num.append(n)
        n=input("请输入一个元素")
    else:
        if(pd(num)):
            print("列表中有重复的元素")
            print(num)
def pd(n):
    if len(n)!=len(set(n)):
        return True
main()

def main():
    sum=0
    num = set("")
    n = input("请输入一个元素")
    while n != "":
        num.add(n)
        n = input("请输入一个元素")
        sum = sum + 1
    else:
        if (len(num)!=sum):
            print("列表中有重复的元素")
            print(num)
        else:
            print("列表中没有重复的元素")
            print(num)
main()

#文本字符分析
txt=input("请输入一条字符串")
counts={}#字典类型
ex=[',','.','?','!',':',';']
for i in txt:
    if i==""or i in ex:
        continue
    else:
        if ord(i)<97:
            i=chr(ord(i)+32)#将大写字母转化成小写
        counts[i]=counts.get(i,0)+1#设置字典key（i）的value值，get方法是键存在则返回相应值，否则返回默认值0然后实现在原来基础上加一
items=list(counts.items())#list方法是将元组转换成列表，items()方法是返回所有的键值对
items.sort(key=lambda x:x[1],reverse=True)#对元组的排序算法：key=lambda不变 x:x[1]表示按照列表中第二个元素排序即那个出现的次数，reverse=True表示倒序输出
for u in range(len(items)):
    alpha,count=items[u]#分别取出列表的第一个和第二个元素
    print("{}->{}".format(alpha,count))

#生日悖论分析
from random import *
def randbirth():
    mon=randint(1,12)
    if mon in[1,3,5,7,8,10,12]:
        day=randint(1,31)
    elif mon==2:
        day=randint(1,28)
    else:
        day=randint(1,30)
    return mon*100+day
def main():
    ls=[]
    for i in range(23):
        ls.append(randbirth())
    if len(ls)==len(set(ls)):
        return 1
    else:
        return 0
try:
    poss=0
    n=eval(input("请输入样本数量："))
    for i in range(n):
        if main()==1:
            poss+=1
    print("23个人中至少两个人生日相同的概率是：{}%".format(poss * 100 / n))
except:
    print("输入有误")
"""

