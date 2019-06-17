import requests
from bs4 import BeautifulSoup

def download():
    url = 'http://www.ruiwen.com/wenxue/shici/308871.html'
    req = requests.get(url)
    html = req.text
    bf = BeautifulSoup(html,'lxml')
    texts = bf.find_all('div',class_ = 'content')
    print(texts[0].text.replace('\<p>'*2,'\n\n'))

if __name__ == '__main__':
    download()
#with open('d:\shige.txt','wb') as f:
#    f.write(req.content)