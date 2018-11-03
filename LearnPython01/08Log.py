# -*- coding: utf-8 -*-
'''
Created on 2018��5��31��

@author: Administrator
'''
import time,functools
from _ast import Nonlocal

# 装饰器decorator
# 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间

def metric(fn):
    
    @functools.wraps(fn)
    def getDiff(*args,**kw):        
        x=time.time()
        print("x1:",x)
        fn(*args,**kw)
        y=time.time()
        print("y:",y)
        print('%s executed in %s ms' % (fn.__name__, y-x))
#         return fn(*args,**kw)    
    return getDiff

@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;
@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)

'''
#请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。
def log(fn):
    @functools.wraps(fn)
    def wraper(*args,**kw):
        print('begin call')
        fn(*args,**kw)
        print('end call')    
    return wraper

@log
def f():
    print('执行f')

f()
'''
def log1(text):
    if isinstance(text, str):
        def test(f):
            @functools.wraps(f)
            def wraper(*args,**kw): 
                print(text)       
                return f(*args,**kw)         
            return wraper
        return test
    else:
        @functools.wraps(text)
        def wraper(*args,**kw): 
            print("no test")       
            return text(*args,**kw)         
        return wraper
@log1
def f1():
    print('执行f')

f1()
@log1('execute')
def f():
    pass
f()