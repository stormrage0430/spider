import requests


baseurl = 'https://fanyi.baidu.com/sug'
kw = input("input your search words: ")
data = {
    'kw': kw
}


headers = {
    #使用post，至少包含Content-Length字段
    'Content-Length':str(len(data))
}
#post要求dict类型
rsp = requests.post(baseurl, data=data)

print(rsp.text)
print(rsp.json())

