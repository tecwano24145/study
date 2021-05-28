from urllib import request
from bs4 import BeautifulSoup

url = 'http://www.siteboxs.com/sitebox_list.do?page=6'
req = request.Request(url)
data = request.urlopen(req).read().decode('utf-8')

soup = BeautifulSoup(data,'html5lib')
thumb = soup.find(class_='thumbnails')

all_li = thumb.find_all('li')

for item in all_li:
    title = item.find('div').find(class_='tta').get_text().strip()
    desc = item.find('div').find(class_='tta').get('title').strip()
    icon_file = item.find('div').find(class_='siteIco')['srcurl']
    href = item.find('div').find(class_='sbi2 subnum')['href']
    tags = item.find('div').find_all(class_='c1')
    tag_arr = []
    for tag in tags:
        tag_char = tag.get_text().strip()
        if tag_char:
            tag_arr.append(tag_char)
    tag_text = ','.join(tag_arr)
    print(tag_text)


