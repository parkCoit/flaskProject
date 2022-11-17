import pandas as pd
from sphinx.util import requests

apiDefault = {
    "id": 13, # 프리시즌 x
    "season": "SEASON 2019", #19년도 시즌
    'region': 'https://kr.api.riotgames.com',  # 한국서버를 대상으로 호출

    'key': 'RGAPI-55d661c9-d4a5-4b92-9071-9fe623dac327'  # API KEY
}
request_header = {
    "User-Agent": "Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36(Gecko와 같은 KHTML) Chrome/107.0.0.0 Safari/537.36",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "출처": "https://developer.riotgames.com",
    "X-Riot-토큰": "RGAPI-55d661c9-d4a5-4b92-9071-9fe623dac327"
}
# id , season 해본 결과 401 찍힘
def league_v4_god_league(summoner_id):
    url = f"{apiDefault['region']}/lol/league/v4/entries/by-summoner/{summoner_id}?api_key={apiDefault['key']}"
    return requests.get(url)





if __name__ == '__main__':
    a = print(league_v4_god_league("EOO3HspnQLEzn5t43ZO4TdwIRJbX1rCnDT4DMcaAPz4pXxg").json())
    pd.DataFrame(a)