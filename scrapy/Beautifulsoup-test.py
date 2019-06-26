import requests
from bs4 import BeautifulSoup
import re


html_doc = """
<html>
<head>
    <title>The Dormouse's story</title>
</head>
<body>
<p class="title aq">
    <b>
        The Dormouse's story
    </b>
</p>
<p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 
    and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.
</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc,'html.parser')
#print(soup.title)
#print(soup.title.name)
#print(soup.title.string)
#print(soup.title.parent.name)
#print(soup.p)
#print(soup.p['class'])
#print(soup.a['href'])
#soup.a['href'] = 'http://www.baidu.com/'
#soup.a['name'] = u'百度'
#print(soup.p.contents)
#print(soup.find(id='link3'))
#print(soup.get_text())
#print(soup.a.attrs)
#for link in soup.find_all('a'):
#    print(link.get('href'))

#for child in soup.p.children:
#    print(child)

#for tag in soup.find_all(re.compile("b")):
#    print(tag.name)

#html = soup.contents[0]
#print(html)
#head = soup.contents[0]
#print(head)

#print(soup.a)
#print(soup.a.string)
#print(type(soup.a.string))

#print(soup.head.contents[0])
#print(soup.head.children)

#for child in soup.body.children:
#    print(child)

#for child in soup.descendants:
#    print(child)

#print(soup.find_all('a'))
#print(soup.find_all("a",class_="sister"))

#for tag in soup.find_all(True):
#    print(tag.name)

print(soup.select('#link1'))