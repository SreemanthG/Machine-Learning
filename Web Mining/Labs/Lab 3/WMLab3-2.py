import re
from bs4 import BeautifulSoup
from urllib import request

url = "https://www.w3schools.com/html/default.asp"
html = request.urlopen(url).read().decode('utf8')
#'<!doctype html public "-//W3C//DTD HTML 4.0 Transitional//EN'
raw = BeautifulSoup(html, 'html.parser').get_text()
print(raw)




import requests
import re
from bs4 import BeautifulSoup

#URL = "https://arstechnica.com"

URL = "https://www.dreamhost.com/"

l=[] # queue
visited=[] #visited list
counter=1
l.append(URL) #insert 5 urls
for counter in range(0,20):# 0 to 20
    i=l.pop(0)
    print(i)
    visited.append(i)
    page = requests.get(i)
    soup = BeautifulSoup(page.content, 'html.parser')
    for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
        if link.get('href') not in visited:
            l.append(link.get('href')) 