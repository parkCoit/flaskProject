import googlemaps
import pandas as pd

CRIME_MENUS = ["Exit",  # 0
               "Spec",  # 1
               "Merge",  # 2 여러개의 객체를 하나로 통합
               "Interval",  # 3
               "Norminal",  # 4
               "ordinal",  # 5
               "Partition",  # 6
               "미완성: Fit",  # 7
               "미완성: Predicate"]  # 8
crime_meta = {

}
crime_menu = {
    "1": lambda t: t.spec(),
    "2": lambda t: t.save_police_pos(),
    "3": lambda t: t.interval(),
    "4": lambda t: t.norminal(),
    "5": lambda t: t.ordinal(),
    "6": lambda t: t.target(),
    "7": lambda t: t.partition()
}
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 31 entries, 0 to 30
Data columns (total 11 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   관서명     31 non-null     object
 1   살인 발생   31 non-null     int64 
 2   살인 검거   31 non-null     int64 
 3   강도 발생   31 non-null     int64 
 4   강도 검거   31 non-null     int64 
 5   강간 발생   31 non-null     int64 
 6   강간 검거   31 non-null     int64 
 7   절도 발생   31 non-null     object
 8   절도 검거   31 non-null     object
 9   폭력 발생   31 non-null     object
 10  폭력 검거   31 non-null     object
dtypes: int64(6), object(5)
memory usage: 2.8+ KB
'''


class Crime:
    def __init__(self):
        self.crime = pd.read_csv('./data/crime_in_seoul.csv')
        self.cctv = pd.read_csv('./data/cctv_in_seoul.csv')
        self.pop = pd.read_excel('./data/pop_in_seoul.xls', skiprows=1, usecols=['자치구','합계' ,'한국인','등록외국인','65세이상고령자'])

    '''
    1.스펙보기 
    id = 관서명
    Index(['관서명', '살인 발생', '살인 검거', '강도 발생', '강도 검거', '강간 발생', '강간 검거', '절도 발생',
       '절도 검거', '폭력 발생', '폭력 검거'],
      dtype='object')
    '''"""
        Index(['기관명', '소계', '2013년도 이전', '2014년', '2015년', '2016년'], dtype='object'
        """

    def spec(self):
        [(lambda x: print(f"--- Spec ---"
                          f"\n--- 1.Shape ---\n{x.shape}"
                          f"\n--- 2.Features ---\n{x.columns}"
                          f"\n--- 3.Info ---\n{x.info()}"
                          f"\n--- 4.Case Top1 ---\n{x.head(1)}"
                          f"\n--- 5.Case Bottom1 ---\n{x.tail(3)}"
                          f"\n--- 6.Describe ---\n{x.describe()}"
                          f"\n--- 7.Describe All ---\n{x.describe(include='all')}"))(i) for i in
         [self.crime, self.cctv, self.pop]]

    def save_police_pos(self):
        crime = self.crime
        station_names = []
        for name in crime['관서명']:
            print(f"지역이름: {name}")
            station_names.append(f'서울{str(name[:-1])}경찰서')
        print(f" 서울시내 경찰서는 총 {len(station_names)}개 이다")
        [print(f"{str(i)}") for i in station_names]

        gmaps = (lambda x: googlemaps.Client(key=x))("")
        print(gmaps.geocode("서울중부경찰서", language='ko'))
        print(" ### API에서 주소추출 시작 ### ")
        station_addrs = []
        station_lats = []
        station_lngs = []
        for i, name in enumerate(station_names):
            _ = gmaps.geocode(name, language='ko')
            print(f'name {i} = {_[0].get("formatted_address")}')
            station_addrs.append(_[0].get('formatted_address'))
            _loc = _[0].get('geometry')
            station_lats.append(_loc['location']['lat'])
            station_lngs.append(_loc['location']['lng'])
        gu_names = []
        for name in station_addrs:
            _ = name.split()
            gu_name = [gu for gu in _ if gu[-1] == '구'][0]
            gu_names.append(gu_name)
        crime['구별'] = gu_names
        crime.to_csv('./save/police_pos.csv', index=False)



    def interval(self):
        print(self.pop)


    def norminal(self):
        pass

    def ordinal(self):
        pass

    def target(self):
        pass

    def partition(self):
        pass
