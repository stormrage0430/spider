'''
正则结果Match
'''

import re

s = r'([a-z]+)([a-z]+)'
pattern = re.compile(s,re.I)#忽略大小写
m = pattern.match("Hello world wide web")

s = m.group(0)
print(s)

a = m.span(0)
print(a)

s = m.group(1)
print(s)

a = m.span(1)
print(a)

s = m.groups()
print(s)