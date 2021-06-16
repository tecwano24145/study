import requests
import pymysql
import uuid
import os
import datetime

now = datetime.datetime.now()

db = pymysql.connect(
    host="127.0.0.1",
    user="yanying",
    password="123456",
    database="crawler",
    charset='utf8'
)
cursor = db.cursor(cursor=pymysql.cursors.DictCursor)

query = "SELECT sour_id,github_cover FROM br_crawler2 c where github_cover is not null and github_sour_cover is null limit 500"
cursor.execute(query)

results = cursor.fetchall()
if not results:
    exit()

for item in results:
    print(item['sour_id'])
    if item['github_cover'][-3:]=='gif':
        query = "update br_crawler2 set github_sour_cover='{}' where sour_id='{}'".format('1', item['sour_id'])
        cursor.execute(query)
        db.commit()
        continue
    file_dir = now.strftime("%Y%m") + "/27"
    file_name = str(uuid.uuid1())
    file_path = file_dir + '/' + file_name.replace('-', '') + '.png'

    try:
        data = requests.get(item['github_cover']).content

        if not os.path.exists(file_dir):
            os.makedirs(file_dir)
        with open(file_path, 'wb') as f:
            f.write(data)
            query = "update br_crawler2 set github_sour_cover='{}' where sour_id='{}'".format(file_path, item['sour_id'])
            cursor.execute(query)
            db.commit()
            print(file_path)

    except (Exception) as e:
        print(e)
