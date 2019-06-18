from bs4 import BeautifulSoup
import requests
import bs4


def get_html(url):
    try:
#url = 'http://www.zuihaodaxue.com/shengyuanzhiliangpaiming2018.html'
        r = requests.get(url,timeout=20)
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return None


#r.encoding = r.apparent_encoding
#html = r.text
def get_data(html,list):
    soup = BeautifulSoup(html,'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            td = tr('td')
#        print(td)
            t = [td[0].string,td[1].string,td[2].string,td[3].string]
            list.append(t)
def wirte_data(ulist,num):
    for i in range(num):
        u = ulist[i]
        with open('d:/python/daxue.txt','a') as data:
            print(u,file=data)

if __name__ == "__main__":
    list = []
    url = 'http://www.zuihaodaxue.com/shengyuanzhiliangpaiming2018.html'
    html = get_html(url)
    get_data(html,list)
    wirte_data(list,20 )