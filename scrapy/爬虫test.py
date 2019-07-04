import re
import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':

#    url = 'http://www.daomubiji.com/dao-mu-bi-ji-1'
    url = 'http://www.daomubiji.com/qi-xing-lu-wang-01.html'
#    url = 'http://book.zongheng.com/showchapter/775517.html'
    head = {}
    chapter_urls= []
    head[
        'User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    req = requests.get(url, headers=head)
    req.encoding = req.apparent_encoding
    html = req.text


    soup = BeautifulSoup(html, 'lxml')
    title = soup.find_all("h1",class_="article-title")[0]
#    print(title.string)
#    soup_texts = soup.find_all('div', class_="excerpts")
    soup_texts = soup.find_all('article', class_="article-content")
#    title = soup_texts.find_all("h1", class_="article-title").string
#    print(title)
#    soup_texts = soup.find_all('div',class_="excerpts")
#    soup_texts = soup.find_all("article", class_ ="excerpt excerpt-c3")
    for article in soup_texts:
        ps = article.find_all('p')
        for p in ps:
            print(p.string)
 #       print(ps.string)
#   打印出标题和url 链接
#    for link in soup_texts:
#        links = link.find_all('a',href=re.compile("qi-xing-lu-wang"))
#        for urls in links:
#            chapter_urls.append(urls['href'])
#            print(chapter_urls)
 #           print(urls.string + ': ',urls['href'])