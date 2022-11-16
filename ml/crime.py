
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

CRIME_MENUS = ["Exit", #0
                "Spec",#1
                "cctv_spec",#2
                "Interval",#3 18세이상만 사용함
                "Norminal",#4
                "ordinal",#5
                "Partition",#6
                "미완성: Fit",#7
                "미완성: Predicate"]#8
crime_meta = {

}
crime_menu = {
    "1" : lambda t: t.spec(),
    "2" : lambda t: t.cctv_spec(),
    "3" : lambda t: t.interval_variables(),
    "4" : lambda t: t.norminal_variables(),
    "5" : lambda t: t.ordinal_variables(),
    "6" : lambda t: t.target(),
    "7" : lambda t: t.partition()
}
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5110 entries, 0 to 5109
Data columns (total 12 columns):
 #   Column             Non-Null Count  Dtype  
---  ------             --------------  -----  
 0   id                 5110 non-null   int64  
 1   gender             5110 non-null   object 
 2   age                5110 non-null   float64
 3   hypertension       5110 non-null   int64  
 4   heart_disease      5110 non-null   int64  
 5   ever_married       5110 non-null   object 
 6   work_type          5110 non-null   object 
 7   Residence_type     5110 non-null   object 
 8   avg_glucose_level  5110 non-null   float64
 9   bmi                4909 non-null   float64
 10  smoking_status     5110 non-null   object 
 11  stroke             5110 non-null   int64  
dtypes: float64(3), int64(4), object(5)
memory usage: 479.2+ KB
None
'''
class Crime:

    def __init__(self):
        self.crime = pd.read_csv('./data/crime_in_seoul.csv')
        self.cctv = pd.read_csv('./data/cctv_in_seoul.csv')

    '''
    1.스펙보기 
    id = SERIALNO  
    Index(['관서명', '살인 발생', '살인 검거', '강도 발생', '강도 검거', '강간 발생', '강간 검거', '절도 발생',
       '절도 검거', '폭력 발생', '폭력 검거'],
      dtype='object')
    '''

    def spec(self):
        pd.set_option('display.max_columns',None) # 전체보기
        pd.set_option('display.max_rows', None)
        print(" --- 1.Shape ---")
        print(self.crime.shape)
        print(" --- 2.Features ---")
        print(self.crime.columns)
        print(" --- 3.Info ---")
        print(self.crime.info())
        print(" --- 4.Case Top1 ---")
        print(self.crime.head(1))
        print(" --- 5.Case Bottom1 ---")
        print(self.crime.tail(3))
        print(" --- 6.Describe ---")
        print(self.crime.describe())
        print(" --- 7.Describe All ---")
        print(self.crime.describe(include='all'))

        """
        Index(['기관명', '소계', '2013년도 이전', '2014년', '2015년', '2016년'], dtype='object'
        """

    def cctv_spec(self):
        print(" --- 1.Shape ---")
        print(self.cctv.shape)
        print(" --- 2.Features ---")
        print(self.cctv.columns)
        print(" --- 3.Info ---")
        print(self.cctv.info())
        print(" --- 4.Case Top1 ---")
        print(self.cctv.head(1))
        print(" --- 5.Case Bottom1 ---")
        print(self.cctv.tail(3))
        print(" --- 6.Describe ---")
        print(self.cctv.describe())
        print(" --- 7.Describe All ---")
        print(self.cctv.describe(include='all'))

    def rename_meta(self):
        self.my_oklahoma = self.crime.rename(columns=crime_meta)
        print(" --- 2.Features ---")
        print(self.crime.columns)

    def interval_variables(self):
        pass

    def norminal_variables(self):
        pass

    def ordinal_variables(self):
        pass

    def target(self):
        pass

    def partition(self):
        pass

