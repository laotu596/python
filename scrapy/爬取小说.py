import re
import requests
from bs4 import BeautifulSoup

def get_book_urls(url):

    head = {}
    book_urls = []
    head[
        'User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    url = "http://www.daomubiji.com"
    req = requests.get(url, headers=head)
    req.encoding = req.apparent_encoding
    html = req.text
    soup = BeautifulSoup(html,'lxml')

    articles = soup.find_all("article",class_='article-content')
    for article in articles:
        links = article.find_all('a',href=re.compile("dao-mu-bi-ji"))
        for link in links:
            book_urls.append(link['href'])

    return book_urls
#book_urls = get_book_urls("http://www.daomubiji.com")



def get_chapter_urls(url):
    chapter_urls = []
    page = requests.get(url)
    page.encoding = page.apparent_encoding
    soup = BeautifulSoup(page.text,'lxml')
    articles = soup.find_all("article",class_="excerpt excerpt-c3")
    for article in articles:
        chapter_urls.append(article.a['href'])
    return chapter_urls

#chapter_urls = get_chapter_urls("http://www.daomubiji.com/dao-mu-bi-ji-1")
#print(chapter_urls)

def get_content(url):
    content = ""
    page = requests.get(url)
    page.encoding = page.apparent_encoding
    soup = BeautifulSoup(page.text,'lxml')
    title = soup.find_all("h1",class_="article-title")[0].string
    content += ("\n" + title + "\n\n")

    articles = soup.find_all("article",class_="article-content")
    for article in articles:
        ps = article.find_all('p')
        for p in ps:
            for string in p.strings:
                content = content + string + '\n'
    return content
#content = get_content("http://www.daomubiji.com/qi-xing-lu-wang-01.html")
#print(content)

def get_article(url):
    book_urls = get_book_urls(url)
    chapter_urls = []
    for url in book_urls:
        chapter_urls.extend(get_chapter_urls(url))

    result = ""

    for chapter_url in chapter_urls:
        content = get_content(chapter_url)
        result += content
#        print(content)

    with open("d:\python\daomubiji.txt","ab+") as fw:
        fw.write(result.encode("utf8"))

get_article("http://www.daomubiji.com/")