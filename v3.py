import urllib.request

import urllib.parse
if __name__ == '__main__':
    url = 'http://www.baidu.com/s'
    wd = input("input your keyword")


    qs = {
        "wd": wd
    }
    # 转换URL编码
    qs = urllib.parse.urlencode(qs)

    fullurl = url + qs
    print(fullurl)
    rsp = urllib.request.urlopen(fullurl)
    html = rsp.read()

    html = html.decode()
    print(html)