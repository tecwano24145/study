# !/usr/bin/env python
# -*- coding:utf-8 -*-
import pymysql
from urllib import request
from bs4 import BeautifulSoup
import time

conn = pymysql.connect(host='127.0.0.1',port= 3306,user = 'yanying',passwd='123456',db='bidianer',charset='UTF8')
cur = conn.cursor()

header = {
    'Cookie':'UM_distinctid=15cca67f9b12a6-098bf0254ccf5b-8373f6a-1fa400-15cca67f9b2636; _opendigg_session=ejQ0Mm5lcnU5bnhEbDgwZ2dUdk43NE52cTIwWlNYMW1kUUZyLzFRdVpuMWREQnRoaCtTak51WVZRU2tGN2pRbmI3Y1had1puYytKK1JmMVBZV2o2OHBENEZkeVk1dkJjVVpXanBtZXdYc3FDTGo2TWE3eDZybUdhQk9ndEEzZlFMYURLQWhIN3ZhZ0FCWW5ZV0NUWWdRPT0tLUFSaEJTVjVURjJjaFpETVVuY05FSmc9PQ%3D%3D--8688d1a74790ff20778cbdb5fc2350ec3a4a6b39; CNZZDATA1260869832=2069363338-1498041906-https%253A%252F%252Fwww.baidu.com%252F%7C1498047315',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Connection':'keep-alive'
}

tags_name = 'common-tools'

i=0
while True:

    url = 'http://www.opendigg.com/tags/{}?sort=3&pn={}'.format(tags_name,i)
    request_data = request.Request(url, headers=header)
    print(i)
    print('---------------')
    data = request.urlopen(request_data).read().decode('utf-8')

    soup = BeautifulSoup(data, 'html5lib')
    items = soup.find(class_='project-list project-item-list').find_all(class_='project-item')
    if len(items) <= 0:
        cur.close()
        conn.close()
        exit()

    for item in items:
        real_url = 'http://www.opendigg.com' + item.get('data-url').strip()
        star_num = item.find(class_='star-num').get_text().strip()
        title = item.find(class_='project-name').get_text().strip()
        summary = item.find(class_='sub-title').get_text().strip()

        query = "insert into br_crawler(name,summary,sour_url,remark,view) values('{}','{}','{}','{}','{}')".format(title, summary, real_url, tags_name, star_num)
        cur.execute(query)
        conn.commit()
        print(title)
    i += 1
    time.sleep(5)

cur.close()
conn.close()

