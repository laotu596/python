import re
import requests
from bs4 import BeautifulSoup

def get_book_urls(url):

    head = {}
    book_urls = []
    head[ 'User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'

    req = requests.get(url, headers=head)
    req.encoding = req.apparent_encoding
    html = req.text
    soup = BeautifulSoup(html,'lxml')
    articles = soup.find_all("div",class_='volume')
    for article in articles:
        links = article.find_all('a',href=re.compile("read.qidian.com/chapter"))
        for link in links:
            book_urls.append('https:' + link['href'])


    return book_urls


def get_content(url):
    content = ""
    page = requests.get(url)
    page.encoding = page.apparent_encoding
    soup = BeautifulSoup(page.text,'lxml')
    title = soup.find_all("h3",class_="j_chapterName")[0].string
#    print(title)
    content += ("\n" + title + "\n\n")

    articles = soup.find_all("div",class_="read-content j_readContent")
    for article in articles:
        ps = article.find_all('p')
        for p in ps:
            for string in p.strings:
                content = content + string + '\n'
    return content

def get_article(url):
    book_urls = get_book_urls(url)
    result = ""
    for urls in book_urls:
        content = get_content(urls)
        result += content
#        print(content)

    with open("d:\python\gesheng.txt","ab+") as fw:
        fw.write(result.encode("utf8"))

get_article("https://book.qidian.com/info/1015493157#Catalog")