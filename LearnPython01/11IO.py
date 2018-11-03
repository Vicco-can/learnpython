# -*- coding: utf-8 -*-
'''
Created on 2018��6��8��

@author: Administrator
'''
from _io import open
from idlelib.iomenu import encoding
from email.policy import default
from pip._vendor.distlib.wheel import _hook
fpath = r'C:\Windows\system.ini'

with open(fpath, 'r') as f:
    s = f.read()
    print(s)
    
    
path = 'F:\python-workspace\\readtest.txt'

def readtxt(path):
    with open(path, 'r') as f:
        str=f.read()
        print(str)
        f.close()
        # readline()读取一行；readlines：读取所有行到一个list；read(size):读取指定大小
def writetxt():
    with open(path,'w') as f:
        f.write('hello,world')
        f.close()
# writetxt()
readtxt(path)    
def writeappend():
    with open(path, 'a') as f:
        f.write('\nthis is second line')
        f.close()

writeappend()
readtxt(path)

csvPath=r'F:\WBFSJ2017E\WBFSJDataGenerate\bin\Debug\InverseLV2csv\54399-AD-2017-08-24LV2.csv'
with open(csvPath, 'r',encoding='utf-8') as f:
    list=f.readlines()
    f.close()
    for num in range(10,25):
        print(list[num])
# 操作文件
# 1.利用os模块编写一个能实现dir -l输出的程序。
import os


dirs=os.listdir(os.path.split(csvPath)[0])
for file in dirs:
    print(file)
    
print(os.path.abspath('.'))
# 2.编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。


def find():
    strinput=str(input("请输入字符串(输入exit表示退出)："))
    if strinput == exit:
        return
    else:
        findFile(strinput)
    

def findFile(strinput):
    result=[]
    dirlist=os.walk('.')
    for root,dirs,files in dirlist:
        for f in files:
            if strinput in f:
#                 print(strinput)
                print(os.path.join(root,f))        
                result.append(f)
    if len(result)==0:
        print('没有找到包含%s的文件'%strinput)
    
    confirm=input('是否继续查询(yes/no)：')
    if confirm=='yes':
        find()
    else:
        return    
find()

import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
        
def json2student(json):
    return Student(json['age'],json['score'],json['name'])

json_str = '{"age": 20, "score": 88, "name": "Bob"}'

print(json.loads(json_str,object_hook=json2student))

s = Student('Bob', 20, 88)
print(json.dumps(s,default=lambda obj:obj.__dict__))

# 对中文进行JSON序列化时，json.dumps()提供了一个ensure_ascii参数，观察该参数对结果的影响
obj = dict(name='小明', age=20)
s = json.dumps(obj)

print(s)

print(json.loads(s))

s=json.dumps(obj, ensure_ascii=True)

