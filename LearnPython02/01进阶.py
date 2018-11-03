import math
from functools import reduce

'''
函数式编程
'''


def add(x, y, f):
    return f(x)+f(y)


print(add(9, 25, math.sqrt))

# map()函数使用


def format_name(s):
    return s[:1].upper()+s[1:].lower()


for name in map(format_name, ['adam', 'LISA', 'barT']):
    print(name)
# print(map(format_name, ['adam', 'LISA', 'barT']).__next__())


# reduce()函数


def prod(x, y):
    return x*y


print(reduce(prod, [2, 4, 5, 7, 12]))


# filter()函数
# 请利用filter()过滤出1~100中平方根是整数的数


def is_sqr(x):
    a = math.sqrt(x)
    return a-math.ceil(a)==0
print(list(filter(is_sqr, range(1, 101))))

