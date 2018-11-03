# -*- coding: utf-8 -*-
'''
Created on 2018��5��30��

@author: Administrator
'''
# 高级特性
# 切片（截取）
#利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
def trim(s):
    
    while s[:1] == ' ':
        s=s[1:]        
    while s[-1:] == ' ':
        s=s[:-1]        
    return s

print(trim("   vi  cco   "))

# 迭代  请使用迭代查找一个list中最小和最大值，并返回一个tuple：
def findMinAndMax(L):
    if L:          
        max = L[0]
        min = L[0]
        for y in L:
            if max < y:                
                max = y
            if min > y:                
                min = y   
        return (max, min)
    else:
        return (None,None)    

print(findMinAndMax([7]))

# 列表生成式
L1 = ['Hello', 'World', 18, 'Apple', None]
L = [s.lower() for s in L1 if isinstance(s, str)]
print(L)

# 生成器
def triangles():
    L = [1]
    n=0
    while n<=10:
        yield L
        L.append(0)
        L = [L[i - 1] + L[i] for i in range(len(L))]
        n=n+1
        
for x in triangles():
    print(x)
    