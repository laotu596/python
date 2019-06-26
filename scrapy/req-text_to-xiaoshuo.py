import requests
from bs4 import BeautifulSoup
import re


url = 'http://longzu5.co'

def get_son_text(strs):
    req = requests.get(url)
    strs = req.text
    soup = BeautifulSoup(strs,'html.parser')

    result = soup.find_all('p')
#print(result)

    title = soup.find('h1','post-title')
    title = title.text
    final_txt = title + '\n'

#print(title.text + '\n')

    for item in result:
        txt = item.text
        final_txt += txt
    final_txt += '\n\n'
    with open('d:\python\luozu1.txt','a',encoding='utf-8')as fw:
        fw.write(final_txt)
#    print(txt)
def get_father_text():
    req = requests.get(url)
    strs = req.text
    soup = BeautifulSoup(strs, 'html.parser')

    ul_soup = soup.find('ul','booklist')
    x = ul_soup.find_all('a')
    section_list = []
    for each in x:
#    print(each)
        ur = url + each.get('href')
        section_list.append(ur)
        section_list.reverse()
#    print(ur)

    for u in section_list:
#    print(u)
        section = requests.get(u)
        sec_txt = section.text
        get_son_text(sec_txt)
#    with open('d:\python\luzu.txt','a',encoding='utf-8')as f:
#        f.write(sec_txt)

if __name__ == '__main__':
    get_father_text()