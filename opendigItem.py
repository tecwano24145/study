# !/usr/bin/env python
# -*- coding:utf-8 -*-
import pymysql
from urllib import request
from bs4 import BeautifulSoup
import time

conn = pymysql.connect(host='127.0.0.1',port= 3306,user = 'yanying',passwd='123456',db='bidianer',charset='UTF8')
cur = conn.cursor(cursor=pymysql.cursors.DictCursor)

header = {
    'Cookie':'UM_distinctid=15cca67f9b12a6-098bf0254ccf5b-8373f6a-1fa400-15cca67f9b2636; _opendigg_session=ejQ0Mm5lcnU5bnhEbDgwZ2dUdk43NE52cTIwWlNYMW1kUUZyLzFRdVpuMWREQnRoaCtTak51WVZRU2tGN2pRbmI3Y1had1puYytKK1JmMVBZV2o2OHBENEZkeVk1dkJjVVpXanBtZXdYc3FDTGo2TWE3eDZybUdhQk9ndEEzZlFMYURLQWhIN3ZhZ0FCWW5ZV0NUWWdRPT0tLUFSaEJTVjVURjJjaFpETVVuY05FSmc9PQ%3D%3D--8688d1a74790ff20778cbdb5fc2350ec3a4a6b39; CNZZDATA1260869832=2069363338-1498041906-https%253A%252F%252Fwww.baidu.com%252F%7C1498047315',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Connection':'keep-alive'
}
i=0
while True:
    query = "SELECT sour_id,sour_url FROM br_crawler where is_crawler='0' limit 10"
    cur.execute(query)
    lists = cur.fetchall()

    if lists.__len__() <= 0:
        cur.close()
        conn.close()
        exit()

    for item in lists:
        print(i)
        i += 1
        
        request_data = request.Request(item['sour_url'], headers=header)
        try:
            data = request.urlopen(request_data).read().decode('utf-8')
            soup = BeautifulSoup(data, 'html5lib')
            items = soup.find(class_='detail-github-widget').get('data-repo')

            github_url = 'https://github.com/' + items

            github_content = request.urlopen(github_url).read().decode('utf-8')
            github_soup = BeautifulSoup(github_content, 'html5lib')
            github_title = github_soup.find(class_='repository-meta-content').find('a')

            office_url = ''
            if (github_title):
                office_url = github_title.get('href')

            sql = "update br_crawler set official_url='{}',github_url='{}',is_crawler='{}' where sour_id='{}'".format(
                office_url, github_url, 1, item['sour_id'])
            cur.execute(sql)
            conn.commit()
            print(item['sour_url'])
            print(office_url)
            print('====================')
        except (Exception)as e:
            sql = "update br_crawler set is_crawler='{}' where sour_id='{}'".format(2, item['sour_id'])
            cur.execute(sql)
            conn.commit()
            print(e)

cur.close()
conn.close()

