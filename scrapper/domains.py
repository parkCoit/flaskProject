
from dataclasses import dataclass

import pandas as pd
from bs4 import BeautifulSoup



"""
class BugsMusic:
    def __init__(self, url): # DB 까지 생각
        self.url = url
        self.headers = {'User-Agent': 'Mozilla/5.0'}

    def scrap(self):
        soup = BeautifulSoup(urlopen(self.url), 'lxml') # lxml 은 haar에서의 xml 느낌
        _ = 0 # 가져오지 않고 그 자리에서 사용한다
        title = {"class" : "title"} # 해시
        artist = {"class" : "artist"}
        titles = soup.find_all(name="p", attrs=title)
        artists = soup.find_all(name="p", attrs=artist)
        [print(f"{i}. {j.find('a').text} {k.find('a').text}")
         for i, j, k  in zip(range(1, len(titles)+1),titles,artists)]


class Melon:
    def scraps(self):
        req = urllib.request.Request(self.url, headers=self.headers)
        soup = BeautifulSoup(urlopen(req), 'lxml')
        _ = 0
        title = {"class": "rank01"}
        artist = {"class": "rank03"}
        titles = soup.find_all(name="div", attrs=title)
        artists = soup.find_all(name="div", attrs=artist)
        [print(f" {i}등: 제목 : {j.find('a').text} 이름 : {k.find('a').text}")
         for i, j, k in zip(range(1, len(titles) + 1), titles, artists)]

"""
@dataclass
class Scrap:
    html = ""
    parser = ""
    domain = ""
    query_string = ""
    headers = {}
    tag_name = ""
    fname = ""
    class_names = []
    artists = []
    titles = []
    diction = {}
    df = None

    def dict_to_dataframe(self):
        self.df = pd.DataFrame.from_dict(self.diction, orient='index') #orient='index'는 index를 자동 선언



    def dataframe_to_csv(self, fname):
        path = './save/'+fname
        self.df.to_csv(path, sep=',', na_rep="NaN", header=None)


