import os
print(os.getcwd())#返回当前得工作目录
lst=os.listdir("../暑假")#把暑假中所有的文件打印出来，文件在暑假里所以加上。。/
#作用是返回指定路径下的文件和目录信息
print(lst)
#os.mkdir("newdir")#创建目录
#os.makedirs("A/B/C")#创建多级目录
#os.rmdir("newdir")#删除目录newdir
#os.removedirs("A/B/C")#移除多级目录
#os.chdir("E:\\bip\\chap15")#改变当前目录