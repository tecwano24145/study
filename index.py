import urllib
from urllib import request,parse

url = 'http://bidian.com/my/get-bag-sour'
data = {
    'page':1,
    'id':200,
    '_csrf_bidian':'d05FSElZLVQaNDUNM28aFUYJCBgWLW8nPykmACcTAGQQLBo6AQhOZw==',
    'searchContent':''
}

data = parse.urlencode(data).encode('utf-8')

header = {
    'Cookie':'bidian-frontend=ai7fm1u52jdqoq3ia86jsg6lc0; _csrf_bidian=7ae0ca50e41cdcb1ecf791f3b5bc1cdc92496ecb7e8812407094516840f4caf1a%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22_csrf_bidian%22%3Bi%3A1%3Bs%3A32%3A%22mzpEz67A1GMP_tBsHgcHnJ-0gb_rHQc3%22%3B%7D; _identity-frontend=d4bb9d50f560ccd84b91c580081806796ece9aa4b60d151c9432dadc4ffc35b5a%3A2%3A%7Bi%3A0%3Bs%3A18%3A%22_identity-frontend%22%3Bi%3A1%3Bs%3A47%3A%22%5B23%2C%228cEq5U-kTaaxxlqAzW2rFI1LqWwDqtQ1%22%2C2592000%5D%22%3B%7D',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Referer':'http://bidian.com/my',
    'Connection':'keep-alive',
    #'X-CSRF-Token':'d05FSElZLVQaNDUNM28aFUYJCBgWLW8nPykmACcTAGQQLBo6AQhOZw==',
    #'X-Requested-With':'XMLHttpRequest'
}

request_data = request.Request(url,headers=header,data=data)

data = request.urlopen(request_data).read()
data = data.decode('UTF-8')
print(data)