# -*- coding: utf-8 -*-
'''
Created on 2018��5��30��

@author: Administrator
'''
# 测试if
s=input("Please input:")
a=int(s)
if a>=18:
    print("adult")
elif a>=6:
    print("teenager")
else:
    print("kid")

# 练习：
# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
# 
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖

def getHealth(h,w):
    bmi = w/(h*h)
    if bmi < 18.5:
        print("过轻")
    elif bmi >= 18.5 and bmi < 25:
        print("正常")
    elif bmi >= 25 and bmi < 28:
        print("过重")
    elif bmi >=28 and bmi <= 32:
        print("肥胖")
    else:
        print("严重肥胖")
    
# H = float(input("请输入身高："))
# W = float(input("请输入体重："))
# getHealth(H, W)


# 循环 1) for...in  2) while
sum = 0
for x in range(101):
    sum = sum + x
print(sum)

# 利用循环依次对list中的每个名字打印出Hello, xxx!
L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print(name)

#
n = 0
while n < 20:
    n=n+1
    if n % 2==0:
        continue
    elif n > 10:
        break
    print(n)
