'''
ajax
'''
from urllib import  request
import json

url = "https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=&start=0&genres=%E5%8A%A8%E4%BD%9C"

rsp = request.urlopen(url)
data = rsp.read().decode()
data = json.loads(data)
print(data)