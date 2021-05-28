from urllib import request
import re

import sys
from bs4 import BeautifulSoup

url = "http://daily.zhihu.com/"
def getHtml(url):
    headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"}
    req = request.Request(url , headers=headers)
    data = request.urlopen(req).read()
    return data.decode('utf-8')

def getUrls(html):
    pattern = re.compile('<a href="/story/(.*?)"') # 正则表达式编译成正则表达式对象，提高效率
    items = re.findall(pattern , html)
    urls = []
    for item in items:
        urls.append("http://daily.zhihu.com/story/"+item)
    return urls

def getContents(url):
    html = getHtml(url)
    pattern = re.compile(r'<h1 class="headline-title">(.*?)</h1>')
    title = re.findall(pattern,html)
    print(title)

html = getHtml(url)
soup = BeautifulSoup(html,'html5lib')

print(soup.find_all('a'))