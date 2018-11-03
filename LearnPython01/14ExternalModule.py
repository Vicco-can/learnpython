# -*- coding: utf-8 -*-

# requests
import requests

r = requests.get('https://www.douban.com/')
# print(r.text)


# chardet
import chardet
print(chardet.detect('你好，中国'.encode('utf-8')), chardet.detect('你好，中国'.encode('utf-8'))['encoding'])


# psutil
# psutil获取系统信息，系统管理员和运维小伙伴不可或缺的必备模块
import psutil

print(psutil.cpu_count())
print(psutil.cpu_count(logical=False))
print(psutil.cpu_times())
print(psutil.disk_usage('/'))
print(psutil.net_if_addrs())
print(psutil.net_connections())
print(psutil.pids())
print(psutil.Process(0).name())
# print(psutil.test())