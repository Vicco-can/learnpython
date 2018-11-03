# -*- coding: utf-8 -*-

import re


def is_valid_email(addr):

	s = r'(^[a-zA-z0-9\.]+)\@([a-zA-z]+)(.com)$'
	if re.match(s, addr):
		return True
	else:
		return False


assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')

def name_of_email(addr):

	s = re.compile(r'^<?([\w\s]+)>?\s*([a-zA-Z]*)@([a-zA-z]+)\.(\w+$)')
	r = re.compile(r'^<[\w\s]*>')

	print(s.match(addr).groups())
	return s.match(addr).group(1)


# 测试:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')