import re

import googlemaps
import numpy as np
import pandas as pd
import pickle
import folium
import json

from sklearn import preprocessing

CRIME_MENUS = ["Exit",  # 0
               "Show spec",  # 1
               "Save Police Position",  # 2
               "Save CCTV Population",  # 3
               "Save Police Norm",  # 4
               "Folium Example",  # 5
               "Partition",  # 6
               "미완성: Fit",  # 7
               "미완성: Predicate"]  # 8
crime_meta = {

}
crime_menu = {
    "1": lambda t: t.spec(),
    "2": lambda t: t.save_police_pop(),
    "3": lambda t: t.save_cctv_pos(),
    "4": lambda t: t.save_police_norm(),
    "5": lambda t: t.folium_example(),
    "6": lambda t: t.target(),
    "7": lambda t: t.partition(),
    "8": lambda t: t.save_cctv_pos()
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
        cols = ['절도 발생', '절도 검거', '폭력 발생', '폭력 검거'] # str 값 존재하는 col
        self.crime[cols] = self.crime[cols].replace(',', '', regex=True).astype(int) #str 전환 후 int 전환

        self.cctv = pd.read_csv('./data/cctv_in_seoul.csv')
        self.pop = pd.read_excel('./data/pop_in_seoul.xls', skiprows=[0,2] , usecols=['자치구', '합계', '한국인', '등록외국인', '65세이상고령자'])
        self.crime_rate_columns = ['살인검거율', '강도검거율', '강간검거율', '절도검거율', '폭력검거율']
        self.crime_columns = ['살인', '강도', '강간', '절도', '폭력']
        self.arrest_columns = ['살인 검거', '강도 검거', '강간 검거', '절도 검거', '폭력 검거']
        self.us_states = './data/us-states.json'
        self.us_unemployment = pd.read_csv('./data/us_unemployment.csv')
        print(self.us_unemployment)

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

    def save_police_pop(self):
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
        # 구와
        crime.loc[crime['관서명'] == '혜화서', ['구별']] == '종로구'
        crime.loc[crime['관서명'] == '서부서', ['구별']] == '은평구'
        crime.loc[crime['관서명'] == '강서서', ['구별']] == '양천구'
        crime.loc[crime['관서명'] == '종암서', ['구별']] == '성북구'
        crime.loc[crime['관서명'] == '방배서', ['구별']] == '서초구'
        crime.loc[crime['관서명'] == '수서서', ['구별']] == '강남구'
        crime.to_pickle('./save/police_pos.pkl')
        print(pd.read_pickle('./save/police_pos.pkl'))

    def save_cctv_pos(self): # ratio -> norminal
        cctv = self.cctv
        pop = self.pop
        cctv.rename(columns={cctv.columns[0]: '구별'}, inplace=True) # inplace 다른 공간에서 변경을 유지함
        pop.rename(columns={
            pop.columns[0]: '구별',
            pop.columns[1]: '인구수',
            pop.columns[2]: '한국인',
            pop.columns[3]: '외국인',
            pop.columns[4]: '고령자'
        }, inplace=True)
        print('*'*100)
        pop.drop(index=26, inplace=True)
        print(pop)
        pop['외국인비율'] = pop['외국인'].astype(int) / pop['인구수'].astype(int) * 100
        pop['고령자비율'] = pop['고령자'].astype(int) / pop['인구수'].astype(int) * 100
        cctv.drop(["2013년도 이전", "2014년","2015년", "2016년"], axis=1, inplace=True)
        print(cctv)
        cctv_pop = pd.merge(cctv, pop,on='구별') # merge 할때 col에서 '구별'
        cor1 = np.corrcoef(cctv_pop['고령자비율'], cctv_pop['소계']) # 상관관계 np.corrcoef()
        cor2 = np.corrcoef(cctv_pop['외국인비율'], cctv_pop['소계'])
        print(f'고령자비율과 CCTV의 상관계수 {str(cor1)} \n'
              f'외국인비율과 CCTV의 상관계수 {str(cor2)} ')
        """
         고령자비율과 CCTV 의 상관계수 [[ 1.         -0.28078554]
                                     [-0.28078554  1.        ]] 
         외국인비율과 CCTV 의 상관계수 [[ 1.         -0.13607433]
                                     [-0.13607433  1.        ]]
        r이 -1.0과 -0.7 사이이면, 강한 음적 선형관계,
        r이 -0.7과 -0.3 사이이면, 뚜렷한 음적 선형관계,
        r이 -0.3과 -0.1 사이이면, 약한 음적 선형관계,
        r이 -0.1과 +0.1 사이이면, 거의 무시될 수 있는 선형관계,
        r이 +0.1과 +0.3 사이이면, 약한 양적 선형관계,
        r이 +0.3과 +0.7 사이이면, 뚜렷한 양적 선형관계,
        r이 +0.7과 +1.0 사이이면, 강한 양적 선형관계
        고령자비율 과 CCTV 상관계수 [[ 1.         -0.28078554] 약한 음적 선형관계
                                    [-0.28078554  1.        ]]
        외국인비율 과 CCTV 상관계수 [[ 1.         -0.13607433] 거의 무시될 수 있는
                                    [-0.13607433  1.        ]]                        
         """
        cctv_pop.to_pickle('./save/cctv_pop.pkl')
        print(pd.read_pickle('./save/cctv_pop.pkl'))

    def save_police_norm(self): # norm 정규화
        police_pos = pd.read_pickle('./save/police_pos.pkl')
        police = pd.pivot_table(police_pos, index='구별', aggfunc=np.sum) # aggfunc 집계함수 리듀서
        police['살인검거율'] = (police['살인 검거'].astype(int) / police['살인 발생'].astype(int)) * 100
        police['강도검거율'] = (police['강도 검거'].astype(int) / police['강도 발생'].astype(int)) * 100
        police['강간검거율'] = (police['강간 검거'].astype(int) / police['강간 발생'].astype(int)) * 100
        police['절도검거율'] = (police['절도 검거'].astype(int) / police['절도 발생'].astype(int)) * 100
        police['폭력검거율'] = (police['폭력 검거'].astype(int) / police['폭력 발생'].astype(int)) * 100
        police.drop(columns={'살인 검거','강도 검거','강간 검거','절도 검거','폭력 검거'},axis=1, inplace=True)
        print(police)
        for i in self.crime_rate_columns:
            police.loc[police[i] > 100, 1] = 100 # 데이터값의 기간 오류로 100을 넘으면 100으로 계산
        police.rename(columns={
            '살인 발생': '살인',
            '강도 발생': '강도',
            '강간 발생': '강간',
            '절도 발생': '절도',
            '폭력 발생': '폭력'
        }, inplace=True)
        x = police[self.crime_rate_columns].values
        print(x)
        min_max_scalar = preprocessing.MinMaxScaler()
        """
        스케일링은 선형변환을 적용하여
        전체 자료의 분포를 평균 0, 분산 1이 되도록 만드는 과정
        """
        x_scaled = min_max_scalar.fit_transform(x.astype(float))
        """
        정규화 normalization
        많은 양의 데이터를 처리함에 있어 데이터의 범위(도메인)를 일치시키거나
        분포(스케일)를 유사하게 만드는 작업
        """
        police_norm = pd.DataFrame(x_scaled, columns=self.crime_columns, index=police.index)
        print(police_norm)

        police_norm[self.crime_columns] = police[self.crime_rate_columns]
        police_norm['범죄'] = np.sum(police_norm[self.crime_rate_columns], axis=1)
        police_norm['검거'] = np.sum(police_norm[self.crime_columns], axis=1)
        police_norm.to_pickle('./save/police_norm.pkl')
        print(pd.read_pickle('./save/police_norm.pkl'))



    def folium_example(self): # 지도 folium 샘플
        us_states = self.us_states
        us_unemployment = self.us_unemployment

        url = "https://raw.githubusercontent.com/python-visualization/folium/master/examples/data"

        state_geo = f"{url}/us-states.json"
        state_unemployment = f"{url}/US_Unemployment_Oct2012.csv"
        state_data = pd.read_csv(state_unemployment)

        bins = list(us_unemployment["Unemployment"].quantile([0, 0.25, 0.5, 0.75, 1]))  # quantile 4등분
        m = folium.Map(location=[48, -102],zoom_start=5)

        folium.Choropleth(
            geo_data=state_geo, # 지도
            data=state_data, # 데이터
            name="choropleth",
            columns=["State","Unemployment"], # col
            key_on="feature.id",
            fill_color="BuGn",
            fill_opacity=0.6, # 투명도
            line_opacity=0.5, # 선
            legend_name='Unmployment Rate (%)',
            bins=bins,
            reset = True
        ).add_to(m)
        m.save("./save/us_unemployment.html")



    def norminal(self):
        pass

    def ordinal(self):
        pass

    def target(self):
        pass

    def partition(self):
        pass
