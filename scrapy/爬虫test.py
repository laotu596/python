import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':

  #  url = 'http://www.136book.com/mieyuechuanheji/'
    url = 'http://www.cishuge.com/read/0/771/'
    head = {}
    head[
        'User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    req = requests.get(url, headers=head)
    req.encoding = req.apparent_encoding
    html = req.text


    soup = BeautifulSoup(html, 'lxml')

    soup_texts = soup.find_all('div', id="readerlist")

    for link in soup_texts:

        print(link)
#        print(link.select('a')[0].text + ': ',link.select('a')[0]['href'])
        print(link.select('a')['href'])
#        for a in a_bf:
#            print(a.get('href'))