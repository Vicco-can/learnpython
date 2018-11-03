# -*- coding：utf-8 -*-
# datetime
# 练习：假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，
# 以及一个时区信息如UTC+5:00，均是str，请编写一个函数将其转换为timestamp：


from datetime import datetime, timezone, timedelta
import re

def to_timestamp(strdtime, strutc):
	dt = datetime.strptime(strdtime, '%Y-%m-%d %H:%M:%S')
	print(dt)
	r = r'^UTC([+-]\d+)\:(00$)'
	print(re.match(r, strutc).groups())
	result_dt = dt.replace(tzinfo=timezone(timedelta(hours=int(re.match(r, strutc).group(1)))))
	print(result_dt)

	result_tS = result_dt.timestamp()
	print(result_tS)
	return result_tS

# 测试:
# t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
# assert t1 == 1433121030.0

t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1
t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')

# 摘要算法hashlib
import hashlib

db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

def login(user, password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    if md5.hexdigest() == db[user]:
        return True
    else:
        return False


# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')

# itertools

import itertools


def pi(N):
	#' 计算pi的值 '
	# step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
	natuals = itertools.count(1, 2)

	# step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
	ns = list(itertools.takewhile(lambda x: x <= 2*N-1, natuals))
	print(ns)
	# step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
	ns1 = list(map(lambda x: 4/x if x % 4 == 1 else -4/x, ns))
	print(ns1)
	# step 4: 求和:
	return sum(list(ns1))


# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')

# urllib
# 练习#
# 利用urllib读取JSON，然后将JSON解析为Python对象

from urllib import request
import json


def fetch_data(url):
	with request.urlopen(url) as f:
		data = json.load(f)
		# print(data)
	return data

URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json'
data = fetch_data(URL)
print(data)
assert data['query']['results']['channel']['location']['city'] == 'Beijing'
print('ok11')

# xml
# 练习
# 请利用SAX编写程序解析Yahoo的XML格式的天气预报，获取天气预报

from xml.parsers.expat import ParserCreate
from urllib import request


class DefaultSaxHandler(object):
	weather = {'city': [], 'forecast': []}
	def start_element(self, name, attrs):
		if name == 'yweather:location':
			self.weather['city']=attrs['city']
		elif name == 'yweather:forecast':
			self.weather['forecast'].append(
				{
					'date':attrs['date'],
					'high':attrs['high'],
					'low':attrs['low']
				}
			)


def parseXml(xml_str):
    # print(xml_str)
	handler = DefaultSaxHandler()
	parser = ParserCreate()
	parser.StartElementHandler = handler.start_element
	parser.Parse(xml_str)
	return handler.weather

url = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'

with request.urlopen(url) as f:
	data = f.read()

result = parseXml(data.decode('utf-8'))
print(result)
assert result['city'] == 'Beijing'
print('xml ok')