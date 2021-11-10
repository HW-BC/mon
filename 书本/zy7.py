'''
import keyword
stopwords='\t\n\r: ()'
functionwords='.('
word=[]
output=''
lastAvailable=['from','import']
last=False
def readFile(path):
    file=open(path,'r',encoding='utf-8')
    string=file.read()
    return string[1:]
def parse(string):
    global word
    global output
    for i in string:
        if i in stopwords:
            wd=''.join(word)
            res=isKeyWord(wd)
            if res ==False:
                if i not in functionwords and last==False:
                    wd=wd.upper()
            if wd in lastAvailable:
                last=True
            else:
                last=False
            output+=wd
            output+=i
            word=[]
        else:
            word.append(i)
def isKeyWord(string):
    if string in keyword.kwlist:
        return True
    return False
def outPutFile():
    file=open('D:\python\one\书本\ceshi1.py','w',encoding="utf-8")
    file.write(output)
string=readFile('D:\python\one\书本\ceshi.py')
parse(string)
outPutFile()
'''
import jieba
import re
import  os;
fo= open("source.py","r",encoding='utf-8').read()

table=["def","for","in","return","print","range"]
words  = jieba.lcut(fo)
fo2=open("source.py","w")
pas=''
for i in range(0,len(words)):

    if words[i] in table:
        pass;

    else:
        words[i]=words[i].upper()
        pas="".join(words)
fo2.write(pas)
fo2.close()