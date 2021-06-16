from urllib import request
import random

request_url = 'http://www.opendigg.com/tags/front-end?sort=3&pn={}'.format(0)

iplist=['70.254.226.206:8080']
proxy_support=request.ProxyHandler({"http":random.choice(iplist)})
opener=request.build_opener(proxy_support)
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36')]
request.install_opener(opener)
response=request.urlopen(request_url)
html=response.read().decode("utf-8")
print(html)