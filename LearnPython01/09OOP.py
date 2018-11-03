# -*- coding: utf-8 -*-
'''
Created on 2018��6��5��

@author: Administrator
'''
# 把下面的Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查参数有效性
class Student(object):
    
    def __init__(self,name,gender):
        self.__name=name        
        if gender.lower() != 'male' and gender.lower() != 'female':
            print('输入有误')
            self.__gender=''
        else:                       
            self.__gender=gender
        
    def get_name(self):
        return self.__name
    
    def get_gender(self):
        return self.__gender
    
    def set_name(self,name):
        
        self.__name=name
        
    def set_gender(self,gender):
        if gender.lower() != 'male' and gender.lower() != 'female':
            print('输入有误')
        else:                        
            self.__gender=gender

bart=Student('Vicco','male')
print(bart.get_gender())
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')

print(type(bart))

# 为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加
class Classmate(object):
    total = 0
    def __init__(self, name):
        self.name = name
        Classmate.total=Classmate.total+1

c1=Classmate('c1')
c2=Classmate('c2')
c3=Classmate('c3')
c4=Classmate('c4')
print(Classmate.total)

# 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution

class Screen(object):
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self,value):
        self._width=value
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self,value):
        self._height=value
    
    @property
    def resolution(self):
        self._resolution=self._height*self._width
        return self._resolution
    
# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')    


# 使用枚举类
from enum import Enum,unique

month=Enum('month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name,member in month.__members__.items():
    print(name, '=>', member, ',', member.value)

# 把Student的gender属性改造为枚举类型，可以避免使用字符串
@unique
class Gender(Enum):
    Male=0
    Female=1
    
class StudentN(object):
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender

# 测试:
bart = StudentN('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')


