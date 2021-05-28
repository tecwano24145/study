# !/usr/bin/env python
# -*- coding:utf-8 -*-
import pymysql

conn = pymysql.connect(host='127.0.0.1',port= 3306,user = 'yanying',passwd='123456',db='bidianer',charset='UTF8')
cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
query = 'select s.sour_id,s.name from br_bag b ' \
        'inner join br_category c on c.cate_id=b.category ' \
        'inner join br_bag_sour bs on bs.bag_id=b.bag_id ' \
        'inner join br_source s on s.sour_id=bs.sour_id ' \
        'where b.delete_flag=0 ' \
        'and c.parent_id=2 ' \
        'and bs.delete_flag=0 ' \
        'and s.delete_flag=0 ' \
        'group by bs.sour_id'
cur.execute(query)
for item in cur.fetchall():
    print(item)

