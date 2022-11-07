import urllib
from urllib.request import urlopen

from bs4 import BeautifulSoup

from scrapper import MusicRanking


def BugsMusic(arg):
    soup = BeautifulSoup(urlopen(f"{arg.domain}{arg.query_string}"), 'lxml')
    _ = 0  # 가져오지 않고 그 자리에서 사용한다
    title = {"class": arg.class_names[0]}  # 해시
    artist = {"class": arg.class_names[1]}
    titles = soup.find_all(name=arg.tag_name, attrs=title)
    artists = soup.find_all(name=arg.tag_name, attrs=artist)
    #디버깅
    [print(f"{i}. {j.find('a').text} {k.find('a').text}")
     for i, j, k in zip(range(1, len(titles) + 1), titles, artists)]
    return arg
    # dict 로 변환
    #diction = {}
    #for i, j in zip(titles, artists):
        #diction[j] = i
    #arg.diction = diction


    # csv 파일로 저장

    #arg.dict_to_dataframe()
    #arg.dataframe_to_csv()

def MelonMusic(url, headers):
    req = urllib.request.Request(url, headers=headers)
    soup = BeautifulSoup(urlopen(req), 'lxml')
    _ = 0
    title = {"class": "rank01"}
    artist = {"class": "rank03"}
    titles = soup.find_all(name="div", attrs=title)
    artists = soup.find_all(name="div", attrs=artist)
    [print(f" {i}등: 제목 : {j.find('a').text} 이름 : {k.find('a').text}")
     for i, j, k in zip(range(1, len(titles) + 1), titles, artists)]