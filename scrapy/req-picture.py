import requests,os
from bs4 import BeautifulSoup


def save_picture_to_local():
    pic_id = 0  # 图片编号
    url = 'http://www.ivsky.com/bizhi/stand_by_me_doraemon_v45983/'
    bs = BeautifulSoup(requests.get(url).content, "lxml")  # 调用lxml作为解析引擎 需要:pip install lxml

    for i in bs.select('.il_img'):
        pic_url = i.find('img')['src']
#    print(pic_url)
        if pic_url.startswith('//'):
            new_url = 'http:' + pic_url
#        print(new_url)
            pic_file = os.path.join('d:/python/'+ str(pic_id) + '.jpg')
            fw = open(pic_file,'wb')
            fw.write(requests.get(new_url).content)
            pic_id += 1
            fw.close()
if __name__ == "__main__":
    save_picture_to_local()