# -*- coding:utf-8 -*-
import pymysql
from pprint import pprint

db = pymysql.connect(
    host="127.0.0.1",
    user="yanying",
    password="123456",
    database="bidianer",
    charset='utf8'
)
cursor = db.cursor(cursor=pymysql.cursors.DictCursor)

sql = 'select * from br_user where user_id=19'

cursor.execute(sql)
result = cursor.fetchall()

for item in result:
    pprint(item['user_email'])

cursor.close()
db.close()