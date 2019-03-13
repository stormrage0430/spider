'''
search
'''
import  re
s = r'\d+'

pattern = re.compile(s)

m = pattern.search("one12two34three56")
print(m.group())

m = pattern.search("one12two34three56",10,40)
print(m.group())

# findall
x = pattern.findall("asdf18dfagrewre456")
print(x)
#finditer
y = pattern.finditer("asdf18dfagrewre456")
print(type(y))
for i in y:
    print(i)

#匹配中文 unicode范围主要在【u4e00-u9fa5】
hello = u'你好世界'
pattern = re.compile(r'[\u4e00-\u9fa5]+')
m = pattern.findall(hello)
print(m)