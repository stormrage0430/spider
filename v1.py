import urllib.request
import chardet
if __name__ == '__main__':
    url = 'https://study.163.com/courses-search?keyword=%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BD%91%E7%BB%9C'
    rsp = urllib.request.urlopen(url)
    html =  rsp.read()
    #利用chardet自动检测
    cs = chardet.detect(html)
    print(type(cs))
    print(cs)

    #使用get取值保证不会出错
    html = html.decode(cs.get("encoding","utf-8"))
    print(html)
