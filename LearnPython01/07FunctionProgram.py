# -*- coding: utf-8 -*-
'''
Created on 2018��5��30��

@author: Administrator
'''
# 函数式编程
#高阶函数：可传入函数作为参数
from _ast import Nonlocal
from test.test_tools.test_unparse import nonlocal_ex
def add(x, y, f):
    return f(x) + f(y)

print(add(-5, 6, abs))

# map、reduce
def f(x):
    return x*x

r=map(f,[1,2,3,4,5])
print(list(r))

print(list(map(str,[1,2,3,4,5])))

# reduce
from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))

# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']

def normalize(name):    
    return  name[:1].upper()+name[1:].lower()

r=map(normalize,['adam', 'LISA', 'barT'])
print(list(r))

# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积
def prod(L):
    def f(x,y):
        return x*y
    return reduce(f, L)
    
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')
    
# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
def str2float(s):
   # DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    l1=s.split('.')[0]
    l2=s.split('.')[1]
    def char2num(s):
        return DIGITS[s]
    def fn(x, y):
        return x * 10 + y
    
    return reduce(fn, map(char2num,l1))+ reduce(fn, map(char2num,l2))/pow(10, len(l2))  

print(str2float('123.456')) 
    
# 斐波那契(fibonacci)数列  
def fibo(n):
    a,b=0,1
    i=0
    while i<n:
        yield b
        a,b=b,a+b
        i=i+1

print(list(fibo(10)))

# filter
# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数
def is_palindrome(n):
    s= str(n)    
    return  s==s[::-1]  

output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))

# 排序 请用sorted()列表分别按名字排序
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):    
    return t[0]

L2 = sorted(L, key=by_name)
print(L2)

def by_score(t):
    return t[1]

L2 = sorted(L, key=by_score)
print(L2)

# 返回函数
# 利用闭包返回一个计数器函数，每次调用它返回递增整数
def createCounter():     
    j = 0     
    def counter():
        nonlocal j
        j += 1           
        return j       
    return counter
    

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA(), counterA(), counterA(), counterA(), counterA())
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
    
# 用匿名函数改造下面的代码
def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1, 20)))
print(L)
L = list(filter(lambda n: n%2==1, range(1, 20)))
print(L)



