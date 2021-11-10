#len计算包含空格吗？
#print(len(" Pytho n "))#答案是：9.包含
'''
import time
scale=10
print("------开始执行------")
for i in range(scale+1):#加一是因为要读11次，从0到十
    a,b="**"*i,'..'*(scale-i)
    c=(i/scale)*100
    print("%{:^3.0f}[{}->{}]".format(c,a,b))#这个3是占位符，表示都占三个位置20空格（三个位置）
    #上面的代码：
    #冒号作用是分割（冒号前部分代表填充的值的标志，后部分代表格式）
    #^：表示居中（参考那个输出的0的位置）
    #3.0f：数值类型保留位数，3位整数（不够的话补空格），0位整数
    time.sleep(0.1)#推迟0.1s后执行下一条语句
print("-----执行结束-----")
#上面是一下子输出好几行


#一行输出实现带刷新的文本进度条：
import time
scale=50
print("执行开始".center(scale//2,'-'))
t=time.perf_counter()#这里python3.8以后就不支持clock（）函数代替成time.pref_counter()
for i in range(scale+1):
    a='*'*i
    b='.'*(scale-i)
    c=(i/scale)*100
    t-=time.perf_counter()
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,-t),end="")
    time.sleep(0.05)
print("\n"+"执行结束".center(scale//2,"-"))
'''

