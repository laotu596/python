import requests
from bs4 import BeautifulSoup

url = "https://movie.douban.com/cinema/nowplaying/xian/"

response = requests.get(url=url)
content = response.text

soup = BeautifulSoup(content,'html.parser')
movie_list = soup.find_all('li',class_='list-item')
#print(moive_list[0])
movies_info = []

for item in movie_list:
    now_movies_dict = {}
    now_movies_dict['title'] = item['data-title']
    now_movies_dict['id'] = item['id']
    now_movies_dict['actors'] = item['data-actors']
    now_movies_dict['director'] = item['data-director']
    movies_info.append(now_movies_dict)

with open('d:/python/movies.txt','w') as f:
    for item in movies_info:
        f.write(str(item) + '\n')