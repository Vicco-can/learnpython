# -*- coding: utf-8 -*-
'''
Created on 2018��5��29��

@author: Administrator
'''
import math


# function
def printHex(x):
    print(hex(x))
n1 = 255
n2 = 1000
printHex((n1))
printHex((n2))

# 练习：定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：ax2 + bx + c = 0的两个解。
def quadratic(a,b,c):
    d = b*b-4*a*c
    if d < 0:
        return "方程无实数根"
    elif d==0:
        return -b/(2*a)
    else:
        x1=(-b+math.sqrt(d))/(2*a)
        x2=(-b-math.sqrt(d))/(2*a)
        return x1,x2
    
r=quadratic(1, 3, -4)
print(r)

# 参数
def product(*num):
    r=1;
    for x in num:
        if not isinstance(x, (float,int)):
            raise TypeError("typeerror")
        else:
            r=r*x    
    return r
num = [5,6,7,9]
print(product(5,6,7))
print(product(*num))
print(product())
# print(product('a',2,5))

# 计算xn次方
def power(x,n=2):
    r=1
    while n>0:
        r=r*x
        n=n-1
    return r

print(power(5, 3))  
print(power(5))

# 关键数参数
def output(name,age,**kw):
    print(name,age,'others:',kw)
        
output('Vicco', 20, hobby='exercise',home='xz')

# 递归函数练习： 编写move(n, a, b, c)函数，
# 它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法
def move(n,a,b,c):
    if n==1:
        print(a,'-->',c)
    else:
        move(n-1,a,c,b)
        print(a,'-->',c)
        move(n-1,b,a,c)

move(3, 'A', 'B', 'C')
        
# 求n!
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))    
#  尾递归优化,解决递归调用栈溢出
def fact1(n):
    return fact_de(n,1)

def fact_de(n,result):
    if n==1:
        return result
    else:
        return fact_de(n-1, n*result)
    
print(fact(5)) 
    