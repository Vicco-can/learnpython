# coding=gbk
'''
Created on 2018��5��27��

@author: Administrator
'''
import os
import requests
#�����ⲿ��requests
print(os.getcwd())
r=requests.get("http://www.baidu.com")
print(r.url)
#�������ַ��� 
print('Hello')
#�������ַ�������
print('''this is first line
    this is second line
    this is third line''')
#�ַ���formatʹ��
name="Tom"
age=18
print("{0} is {1} years old".format(name, age))
#��r''��ʾ''�ڲ����ַ���Ĭ�ϲ�ת��
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