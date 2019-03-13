'''
破解有道词典（js加密）
'''
from urllib import request, parse

def youdao(key):

    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"

    data = {
        "i": "fes",
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": "15521847980198",
        "sign": "826a36a57b8126768d656820960ee01f",
        "ts": "1552184798019",
        "bv": "33a62fdcf6913d2da91495dad54778d1",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTIME",
        "typoResult": "false"
    }
    #需要bytes格式
    data = parse.urlencode(data).encode()
    headers = {
        "Accept":"application/json,text/javascript,*/*;q=0.01",
        #"Accept-Encoding":"gzip,deflate"
        "Accept-Language":"en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
        "Connection": "keep-alive",
        "Content-Length": "253",
        "Content-Type": "application / x - www - form - urlencoded;charset = UTF - 8",
        "Cookie":"OUTFOX_SEARCH_USER_ID=-1650408658@10.169.0.83;JSESSIONID=aaapfxbWn3h1Kfv-3ALLw;OUTFOX_SEARCH_USER_ID_NCOO=1870110407.434047;___rl__test__cookies= 552184798016",
        "Host":"fanyi.youdao.com",
        "Origin":"http://fanyi.youdao.com",
        "Referer":"http://fanyi.youdao.com/",
        "User-Agent":"Mozilla/5.0(WindowsNT10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 72.0.3626.121Safari / 537.36",
        "X-Requested-With":"XMLHttpRequest",

    }

    req = request.Request(url=url, data=data,headers=headers)

    rsp = request.urlopen(req)

    html = rsp.read().decode()
    print(html)

if __name__ == '__main__':
    youdao("fes")