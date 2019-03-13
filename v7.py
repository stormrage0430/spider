'''
使用代理访问
www.xicidaili.com
www.goubanjia.com
'''

from urllib import request, error

if __name__ == '__main__':

    url = "https://www.baidu.com/"

    #使用代理步骤
    #1.设置代理地址
    proxy = {'http':'120.194.18.90:81'}
    #2.创建ProxyHandler
    proxy_handler = request.ProxyHandler(proxy)
    #3.创建Opener
    opener = request.build_opener(proxy_handler)
    #4.安装Opener
    request.install_opener(opener)

    try:
        rsp = request.urlopen(url)
        html = rsp.read().decode()
        print(html)
    except error.URLError as e:
        print(e)
    except Exception as e:
        print(e)