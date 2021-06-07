# -*- coding:utf-8 -*-

import feedparser
from pprint import pprint

#url = 'http://www.pingwest.com/feed/'
url = 'https://segmentfault.com/news/feeds'
data = feedparser.parse(url)

pprint(data.entries[0])

exit()

for item in data.entries:
    pprint(item)
