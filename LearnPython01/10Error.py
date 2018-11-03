# -*- coding: utf-8 -*-
'''
Created on 2018年6月7日

@author: Administrator
'''
# 运行下面的代码，根据异常信息进行分析，定位出错误源头，并修复
from certifi import __main__

from functools import reduce
from _ast import Try
import logging
from symbol import except_clause

def str2num(s):
    return int(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    try:
        r = calc('100 + 200 + 345')
        print('100 + 200 + 345 =', r)
        r = calc('99 + 88 + 7.6')
        print('99 + 88 + 7.6 =', r)
    except Exception as e:
#         logging.exception(e)
        print(e)
    
main()    
'''
# 
# logging.basicConfig(level=logging.INFO)
# s = '0'
# n = int(s)
# logging.info('n = %d' % n)
# print(10 / n)
'''
# 对Student类编写单元测试，结果发现测试不通过，请修改Student类，让测试通过
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_grade(self):
        try:
            if self.score<0 or self.score>100:
                raise ValueError('input error %s' %self.score)        
            if self.score >= 80:
                return 'A'
            if self.score >= 60:
                return 'B'
            return 'C'
        except ValueError as e:
            raise ValueError('ValueError:',e)
import unittest

class TestStudent(unittest.TestCase):

    def test_80_to_100(self):
        s1 = Student('Bart', 80)
        s2 = Student('Lisa', 100)
        self.assertEqual(s1.get_grade(), 'A')
        self.assertEqual(s2.get_grade(), 'A')

    def test_60_to_80(self):
        s1 = Student('Bart', 60)
        s2 = Student('Lisa', 79)
        self.assertEqual(s1.get_grade(), 'B')
        self.assertEqual(s2.get_grade(), 'B')

    def test_0_to_60(self):
        s1 = Student('Bart', 0)
        s2 = Student('Lisa', 59)
        self.assertEqual(s1.get_grade(), 'C')
        self.assertEqual(s2.get_grade(), 'C')

    def test_invalid(self):
        s1 = Student('Bart', -1)
        s2 = Student('Lisa', 101)
        with self.assertRaises(ValueError):
            s1.get_grade()
        with self.assertRaises(ValueError):
            s2.get_grade()

# if __name__ == '__main__':
unittest.main()

# 对函数fact(n)编写doctest并执行
def fact(n):
    
    '''
     Calculate 1*2*...*n
    >>> fact(1)
    1
    >>> fact(10)
    3628800
    >>> fact(-1)
    Traceback (most recent call last):
    ...
    ValueError
    
    '''
    
    if n<1:
        raise ValueError()
    if n==1:
        return 1
    return n*fact(n-1)
if __name__ == __main__:
    import doctest
    doctest.testmod()

# fact(10)
