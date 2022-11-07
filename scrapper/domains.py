
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
class MusicRanking():
    html : str
    soup = BeautifulSoup
    parser : str
    domain : str
    query_string : str
    headers : dict
    tag_name : str
    fname = str
    class_names : []
    artists : list
    titles : list
    dic : dict
    df : None

    @property
    def html(self) -> str: return self._html

    @html.setter
    def html(self, html):  self._html = html

    @property
    def soup(self) -> BeautifulSoup: return self._soup

    @soup.setter
    def soup(self, soup) :  self._soup = soup

    @property
    def parser(self): return self._parser

    @parser.setter
    def parser(self, parser): self._parser = parser

    @property
    def domain(self) -> str :  return self._domain

    @domain.setter
    def domain(self,domain):  self._domain = domain

    @property
    def query_string(self): return self._query_string

    @query_string.setter
    def query_string(self, query_string):  self._query_string = query_string

    @property
    def headers(self): return self._headers

    @headers.setter
    def headers(self, headers):  self._headers = headers

    @property
    def tag_name(self): return self._tag_name

    @tag_name.setter
    def tag_name(self, tag_name):  self._tag_name = tag_name

    @property
    def fname(self): return self._fname

    @fname.setter
    def fname(self, fname):  self._fname = fname

    @property
    def class_names(self): return self._class_names

    @class_names.setter
    def class_names(self, class_names):  self._class_names = class_names

    @property
    def artists(self): return self._artists

    @artists.setter
    def artists(self, artists):  self._artists = artists

    @property
    def titles(self): return self._titles

    @titles.setter
    def titles(self, titles):  self._titles = titles

    @property
    def dic(self): return self._dic

    @dic.setter
    def dic(self, dic):  self._dic = dic

    @property
    def df(self): return self._df

    @df.setter
    def df(self, df):  self._df = df

    def dict_to_dataframe(self):
        self.df = pd.DataFrame.from_dict(self.dic, orient='index')

    def dataframe_to_csv(self):
        ds = Dataset()
        ds.context = './data/'
        path = ds.context+self.fname+'.csv'
        self.df.to_csv(path, sep=',', na_rap="NaN")


