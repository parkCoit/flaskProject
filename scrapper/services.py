import urllib
from urllib.request import urlopen

from bs4 import BeautifulSoup



def BugsMusic(arg):
    soup = BeautifulSoup(urlopen(arg.domain + arg.query_string), arg.parser)
    title = {"class": arg.class_names[0]}
    artist = {"class": arg.class_names[1]}
    titles = soup.find_all(name=arg.tag_name, attrs=title)
    titles = [i.find('a').text for i in titles]
    artists = soup.find_all(name=arg.tag_name, attrs=artist)
    artists = [i.find('a').text for i in artists]
    [print(f"{i}위 {j} : {k}") # 디버깅
     for i, j, k in zip(range(1, len(titles)), titles, artists)]
    diction = {}  # dict 로 변환
    for i, j in enumerate(titles):
        diction[j] = artists[i]
    arg.diction = diction
    arg.dict_to_dataframe()
    arg.dataframe_to_csv("result.csv")  # csv파일로 저장


def MelonMusic(arg):
    req = urllib.request.Request(arg.domain, headers=arg.headers)
    soup = BeautifulSoup(urlopen(req), arg.parser)
    _ = 0
    title = {"class": arg.class_names[0]}
    artist = {"class": arg.class_names[0]}
    titles = soup.find_all(name=arg.tag_name, attrs=title)
    titles = [i.find('a').text for i in titles]
    artists = soup.find_all(name=arg.tag_name, attrs=artist)
    artists = [i.find('a').text for i in artists]
    [print(f"{i}위 {j} : {k}")  # 디버깅
     for i, j, k in zip(range(1, len(titles)+1), titles, artists)]
    diction = {}
    for i, j in enumerate(titles):
        print(j)
        print(i)
        diction[j] =artists[i]
    arg.diction = diction
    arg.dict_to_dataframe()
    arg.dataframe_to_csv("results.csv")