
'''
CookieJar
FileCookieJar(filename, delayload=None,policy=None)使用文件管理
MozillaCookieJar
LwpCookieJar
'''
from urllib import request, parse
from http import  cookiejar
#创建
cookie = cookiejar.CookieJar()
#生成管理器
cookie_handler = request.HTTPCookieProcessor(cookie)

http_handler = request.HTTPHandler()

https_handler = request.HTTPSHandler()

opener = request.build_opener(http_handler, https_handler, cookie_handler)

def login():
    #提取form中url
    url = ""
    #form中input name属性
    data = {
        "email":"",
        "password":""
    }

    data = parse.urlencode(data)

    req = request.Request(url, data=data.encode())
    rsp = opener.open(req)

def getHomePage():
    url = ""
    rsp = opener.open(url)

    html=rsp.read().decode()
    with open("rsp,html", "w") as f:
        f.write(html)


if __name__ == '__main__':
    login()
    '''
    print cookie
    属性name,value,domain,path,expires,size,Http字段
    
    '''
    print(cookie)
    for item in cookie:
        print(item)
        for i in dir(item):
            print(i)