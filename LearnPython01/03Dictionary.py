# -*- coding: utf-8 -*-

'''
Created on 2018��5��29��

@author: Vicco
'''
# 创建一个字典
from _ast import Str
d = {'a':12,'b':13,'c':'Vicco'}

# 操作：取出、赋值、添加、删除、清空
print(d['c'])
print('a' in d)
d['b'] = 'baby'
print("字典："+str(d))
d['d'] = 9  # 添加
print(d)
print(d.get('V'))
print(d.get('V',-1))
print(d.get('a'))
d.pop('d')  #  删除
print(d)
# d[[4,5,6]]='test'
# print(d)   key必须是不可变的
d[(4,5,6)]='test'
print(d)

del d[(4,5,6)]
print(d)

d.clear()
print(d)
del d

# set
s=set([1,2,3])
s.add('c')
s.remove(1)
print(s)
s2=set([3,4,1])
print(s&s2)  # 交集
print(s|s2)  # 并集
a = 'abc'
b=a.replace('abc', 'A')
print(a,b)

list= [1,2,3,2,'c']
print(list)
ss=set().add(list)  #错误哦，不能添加可变key
print(ss)
