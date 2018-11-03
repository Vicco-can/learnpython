# -*- coding: utf-8 -*-
'''
Created on 2018��5��28��

@author: Administrator
'''
import sys

# 格式化
s1 = 72
s2 = 85
r = (85-72)/72
print("r = %.1f" % r )
print('%2d-%02d' % (3, 1))
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125) )

# 浮点型和复数
a=5.66
b=complex(2,a)
print("a's type:",type(a))
print("b's type:",type(b))

print(a/2)
print(9//2)

# 机器浮点型范围
print(sys.float_info)
print("你好\nVicco")

# 创建list
num_list = [1,2,3,4]
str_list = ["asd","dfg","hello"]
mix_list = ["as","sd",34,8]
print("num_list:",num_list)
print("str_list:"+str(str_list))
print("mix_list:",mix_list)

# 访问列表元素
print("1:{0},2:{1},3:{2}".format(num_list[3], str_list[2],mix_list[2]+mix_list[3]))

# 更改删除
num_list[0] = 16
print("num_list:", num_list)
del str_list[1]
print("str_list:"+str(str_list))

print(num_list[-2])  # -代表从右侧定位，数字代表第几位
print(num_list[1:])  # 除第一位后的所有位

print(len(mix_list))  # 长度
print(["Hello"]*4)  # 重组
print([5, 3, 1]+[9, 5, 7])  # 组合

s = ['pyhton','java',['js','css'],'C#']
print(s[2][1])

name_list = ['Sun','Vicco','Kevin','Bob','Jack','lucy']
# 在最后追加一个元素
name_list.append('Amy')
print(name_list)
# 在指定位置插入一个元素
name_list.insert(1, 'Cc')
print(name_list)
# 删除结尾元素
name_list.pop()
print(name_list)
# 删除指定位置元素
name_list.pop(1)
print(name_list)

#练习
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])

# 元组tuple
T = (1,7,['Sun','Vicco'],'f',4)
print(T)
T[2][0] = 'Gao'
print(T)

print(list(T))
print(tuple(L))
print(1 in T)