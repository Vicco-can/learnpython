# Python中的星号：用途及使用方法
'''
使用*和**将参数传递给函数
使用*和**捕捉传递到函数中的参数
使用*接受强制关键字参数
使用*在元组拆包封期间时捕获各项
使用*将迭代器解解包到列表/元组中
用**把词典解包到其他词典
'''

# 1、星号在函数调用中解包参数
# print(*fruits)将fruits列表中的所有项作为单独的参数传递到print函数调用中，
# 我们甚至不需要知道列表包含多少个参数。
A = ['hello', 'Vicco', 'fighting']
print(*A)  # hello Vicco fighting

# **运算符执行类似的操作，但是使用关键字参数。
# **操作符允许我们取一个键值对字典，并将其在函数调用中解包成关键字参数:
date = {'year': 2018, 'month': 11, 'day': 6}
filename = '{year}-{month}-{day}.txt'.format(**date)
print(filename)  # 2018-11-6.txt
print('{year}'.format(**date))  # 2018

# 最常见的地方是执行继承：调用super()通常会用到*和**
# 函数调用中*和**均可被多次使用
# 当使用**多次时，Python中的函数不能多次指定相同的关键字参数，
# 因为每个字典中与**一起使用的键必须是不同的，否则将抛出异常。


# 2、星号用于打包函数中的参数
# *运算符在定义函数时，用于收集所有的位置参数到一个新的元组
def roll(*values):
    return sum(data for data in values)


print(roll(1,2,3,4,5,6))  # 21


# **将捕捉我们赋予这个函数的任何关键字参数，
# 并将其放入一个字典中，该字典将引用attributes参数。
def tag(tag_name, **atttibutes):
    print(tag_name)
    l = [(name, value) for name, value in atttibutes.items()]
    print(*l)


tag('example', height=20, width=10)  # ('height', 20) ('width', 10)


def tag(tag_name, **attributes):
    attribute_list = [f'{name}="{value}"' for name, value in attributes.items()]
    return f"<{tag_name} {' '.join(attribute_list)}>"


print(tag('a', href='www.baidu,com'))


# 同时使用位置参数与强制关键字参数时
# 自Python 3始，有一个特殊的语法来接受强制关键字参数。
# 强制关键字参数是只能使用关键字语法指定的函数参数，这意味着它们不能依据相对位置指定。
# 若要接受强制关键字参数，可在定义函数时于*后放置命名参数：
def get_multiple(*keys, dic, default=None):
    return [
        dic.get(key, default)
        for key in keys
    ]


fruits = {'lemon': 'yellow', 'orange': 'orange', 'tomato': 'red'}
print(get_multiple('tomato', 'lemon', 'apple', dic=fruits, default='Unknown'))
# ['red', 'yellow', 'Unknown']
# 参数dictionary和default在*keys之后出现，
# 这意味着它们只能被指定为关键字参数。如果我们试图依据位置指定它们，我们将收到报错
# print(get_multiple('tomato', 'lemon', 'apple', fruits, 'Unknown'))
# TypeError: get_multiple() missing 1 required keyword-only argument: 'dic'

# 无位置参数只有强制关键字参数时
# 强制关键字参数特性很酷，但若想在不捕获过多的无限位置参数的情况下获取强制关键字参数

def with_previous(iter, *, fillvalue=None):
    previous = fillvalue
    for item in iter:
        yield previous, item
        previous = item


print(list(with_previous([2, 1, 3], fillvalue=0)))

# 星号用于元组解包

fruits1 = ['lemon', 'orange', 'tomato', 'apple']
first, second, *remain = fruits1
print(remain)