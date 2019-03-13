'''
r = "" + (new Date).getTime(),
i = r + parseInt(10 * Math.random(), 10);
 n.md5("fanyideskweb" + e + i + "p09@Bn{h02_BIEe]$P^nG")
ts: r,
bv: t,
r = "" + (new Date).getTime(),
t = n.md5(navigator.appVersion),
"5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
'''

def getSalt():
    import time, random




    salt = int(time.time() * 1000) + random.randint(0,10)
    return salt

def getMD5(v):
    import hashlib
    md5 = hashlib.md5()
    md5.update(v.encode("utf-8"))
    sign = md5.hexdigest()
    return sign

def getSign(key, salt):
    sign = "fanyideskweb" + key + str(salt) + "p09@Bn{h02_BIEe]$P^nG"
    sign = getMD5(sign)
    return sign


def getbv():
    import hashlib
    v="5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
    md5 = hashlib.md5()
    md5.update(v.encode("utf-8"))
    bv = md5.hexdigest()
    return bv

from urllib import request, parse

def youdao(key):

    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"

    salt = getSalt()

    data = {
        "i": key,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": str(salt),
        "sign": getSign(key, salt),
        #"ts": str(ts),
        #"bv": getbv(),
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTIME",
        "typoResult": "false"
    }
    print(data)
    #需要bytes格式
    data = parse.urlencode(data).encode()
    headers = {
        "Accept":"application/json,text/javascript,*/*;q=0.01",
        #"Accept-Encoding":"gzip,deflate",
        "Accept-Language":"en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
        "Connection": "keep-alive",
        "Content-Length": len(data),
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Cookie":"OUTFOX_SEARCH_USER_ID=-1650408658@10.169.0.83;JSESSIONID=aaapfxbWn3h1Kfv-3ALLw;OUTFOX_SEARCH_USER_ID_NCOO=1870110407.434047;___rl__test__cookies=552184798016",
        "Host":"fanyi.youdao.com",
        "Origin":"http://fanyi.youdao.com",
        "Referer":"http://fanyi.youdao.com/",
        "User-Agent":"Mozilla/5.0(WindowsNT10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 72.0.3626.121Safari / 537.36",
        "X-Requested-With":"XMLHttpRequest"

    }

    req = request.Request(url=url, data=data,headers=headers)

    rsp = request.urlopen(req)

    html = rsp.read().decode()
    print(html)

if __name__ == '__main__':
    youdao("boy")