import os.path
print(os.path.abspath("demo15.py"))#获取文件或目录得绝对路径
print(os.path.exists("demo15.py"),os.path.exists("demo18.py"))
#上面一行代码的意思是用于判断文件或目录是否存在
#print(os.path.join("E:\\Python","demo13.py"))#将目录与目录或者文件的名字拼接起来
#print(os.path.split("E:\\Python\\chap5\\demo13.py"))#将目录与文件分开
#print(os.path.splitex("demo13.py"))#将文件与后缀名拆分
#print(os.path.basename("E:\\Python\\chap5\\demo13.py"))#从一个目录中提取文件名
#pr#int(os.path.dirname("E:\\Python\\chap5\\demo13.py"))#从一个路径中提取文件路径，不包括文件名
#print(os.path.isdir("E:\\Python\\chap5\\demo13.py"))#用于判断是否为路径
