from urllib import request, parse

import json

baseurl = 'https://fanyi.baidu.com/sug'
kw = input("input your search words: ")
data = {
    'kw': kw
}
#用parse模块对data进行编码
data = parse.urlencode(data).encode("utf-8")
headers = {
    #使用post，至少包含Content-Length字段
    'Content-Length':len(data)
}
#有了headers.data.url,就可以尝试发出请求
rsp = request.urlopen(baseurl, data=data)

json_data = rsp.read().decode('utf-8')

print(json_data)
#把json字符串转化成字典
json_data = json.loads(json_data)
print(json_data)

for item in json_data['data']:
    print(item['k'], "--", item['v'])