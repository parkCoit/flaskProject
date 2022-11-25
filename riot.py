from urllib.request import urlopen

import requests
from bs4 import BeautifulSoup
from riotwatcher import LolWatcher
import pandas as pd

watcher = LolWatcher("RGAPI-6c6a5bb8-895b-49cd-a5ee-cd6fa9f2a131")
my_region = "kr"
me = watcher.summoner.by_name(my_region, '우엉이우어어엉')

a = pd.DataFrame(me, index=[0])
puuid = me['puuid']
matchid = watcher.match.matchlist_by_puuid(my_region, puuid)

b = watcher.match.timeline_by_match(my_region, matchid[0])
# 매치 api 가져오기

players = ["1","2","3","4","5","6","7","8","9","10"]
totalGolds = []

def TotalGold(p):
    return b['info']['frames'][-1]['participantFrames'][p]["totalGold"]

[totalGolds.append(TotalGold(i)) for i in players]

for i in totalGolds:
    if int(i) < sum(totalGolds)/10:
        print(f"다른 플레이어들에 비해 {int(sum(totalGolds)/10)-int(i)}골드가 적어요\n노력하세요")
    else:
        print(f"평균이상의 골드획득량이에요.")


print(watcher.match.timeline_by_match(my_region, matchid[0]))

