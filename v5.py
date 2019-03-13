#使用request.Request

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

#构造一个实例
req = request.Request(url=baseurl, data=data, headers=headers)

#有了Request请求实例，所有请求信息封装在里面
rsp = request.urlopen(req)

json_data = rsp.read().decode('utf-8')

print(json_data)
#把json字符串转化成字典
json_data = json.loads(json_data)
print(json_data)

for item in json_data['data']:
    print(item['k'], "--", item['v'])