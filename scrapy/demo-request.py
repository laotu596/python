from bs4 import BeautifulSoup
import requests
import bs4

url = 'http://www.zuihaodaxue.com/shengyuanzhiliangpaiming2018.html'
r = requests.get(url)

r.encoding = r.apparent_encoding
html = r.text
soup = BeautifulSoup(html,'html.parser')

for tr in soup.find('tbody').children:
    if isinstance(tr,bs4.element.Tag):
        td = tr('td')
#        print(td)
        t = [td[0].string,td[1].string,td[2].string,td[3].string]
        print(t)