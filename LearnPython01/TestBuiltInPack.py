# coding=gbk
'''
Created on 2018年5月27日

@author: Administrator
'''
import os
import requests
#引入外部包requests
print(os.getcwd())
r=requests.get("http://www.baidu.com")
print(r.url)
#单引号字符串 
print('Hello')
#三引号字符串换行
print('''this is first line
    this is second line
    this is third line''')
#字符串format使用
name="Tom"
age=18
print("{0} is {1} years old".format(name, age))
#用r''表示''内部的字符串默认不转义
print(r'''hello,\n
world''')

n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''
print("s1:",s1)
print("s1:",s2)
print("s1:",s3)
print("s1:",s4)
print("n:",n,"f:",f)