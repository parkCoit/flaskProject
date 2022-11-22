import pandas as pd
from imblearn.under_sampling import RandomUnderSampler
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder


STROKE_MENUS = ["Exit", #0
                "Spec",#1
                "Rename",#2
                "Inteval",#3 18세이상만 사용함
                "Norminal",#4
                "Target",#5
                "Partition",#6
                "미완성: Fit",#7
                "미완성: Predicate"]#8
stroke_meta = {
    'id': '아이디',
    'gender': '성별',
    'age': '나이',
    'hypertension': '고혈압',
    'heart_disease': '심장병',
    'ever_married' : '기혼여부',
    'work_type' : '직종',
    'Residence_type' : '거주형태',
    'avg_glucose_level' : '평균혈당',
    'bmi' : '체질량지수',
    'smoking_status': '흡연여부',
    'stroke': '뇌졸중'
}
stroke_menu = {
    "1" : lambda t: t.spec(),
    "2" : lambda t: t.rename_meta(),
    "3" : lambda t: t.interval_variables(),
    "4" : lambda t: t.categorical_variables(),
    "5" : lambda t: t.target(),
    "6" : lambda t: t.partition()
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

class StrokeService:
    def __init__(self):
        self.stroke = pd.read_csv('../../../../static/data/dam/ml/healthcare-dataset-stroke-data.csv')
        self.my_stroke = None
        self.adult_stoke = None
    '''
    1.스펙보기
    '''
    def spec(self):
        print(" --- 1.Shape ---")
        print(self.stroke.shape)
        print(" --- 2.Features ---")
        print(self.stroke.columns)
        print(" --- 3.Info ---")
        print(self.stroke.info())
        print(" --- 4.Case Top1 ---")
        print(self.stroke.head(1))
        print(" --- 5.Case Bottom1 ---")
        print(self.stroke.tail(3))
        print(" --- 6.Describe ---")
        print(self.stroke.describe())
        print(" --- 7.Describe All ---")
        print(self.stroke.describe(include='all'))
    '''
    2.한글 메타데이터
    '''
    def rename_meta(self):
        self.my_stroke = self.stroke.rename(columns=stroke_meta)
        print(" --- 2.Features ---")
        print(self.my_stroke.columns)




    '''
    3. 타깃변수(=종속변수 dependent, Y값) 설정
    입력변수(=설명변수, 확률변수,X값)
    타깃변수명 : stroke (=뇌졸중)
    타깃 변수값 : 과거에 한 번이라도 뇌졸중이 발병했으면 1, 아니면 0
    '''

    def interval_variables(self): # 타깃 변수 생성
        t = self.my_stroke
        # ID 변수 설정
        print(t['아이디'].dtypes)
        print(t['아이디'].isnull().sum())
        print(len(pd.unique(t['아이디'])))

        # Target 변수 생성
        print("--- Target ---")
        print(t['뇌졸중'].isnull().sum())
        print(t['뇌졸중'].value_counts(dropna=False))
        print(t['뇌졸중'].value_counts(dropna=False, normalize=True))

        # 기타 변수 데이터 처리 구간 변수
        cols = ['나이','평균혈당','체질량지수'] # 구간 변수를 cols에 저장
        print(t[cols].dtypes)
        print(t[cols].isnull().sum())
        print(f'--- 결측값 있는 변수 --- \n {t[cols].isna().any()[lambda x: x]}') # N/A 결측 값
        pd.options.display.float_format = '{:.2f}'.format
        print(t[cols].describe())
        c = t['나이'] > 18  # 18세 이상 True 미만 False
        print(t[c].head(3)) # 18세 미만 데이터셋 제거
        print(len(t[c]))
        print(len(t[c])/len(t) )
        self.adult_stoke = t[c]   # 데이터프레임 t[c]를 t1에 저장
        print(f'성인 객체 스펙 \n{self.adult_stoke.shape}')
        # 평균혈당 232.64이하와 체질량지수 60.3이하를 이상치로 규정하고 제거함
        t = self.adult_stoke
        c1 = t['평균혈당'] <= 232.64
        c2 = t['체질량지수'] <= 60.3
        self.adult_stoke = self.adult_stoke[c1 & c2]
        print(f'이상치 제거한 성인객체스펙 \n{self.adult_stoke.shape}')

    '''
        4.범주형 = ['성별', '심장병', '기혼여부', '직종', '거주형태',
                    '흡연여부', '뇌졸중']
    '''
    # 기타 변수 데이터 처리 범주형 변수  고혈압 심장병 type int64  나머지변수 object
    def categorical_variables(self):
        t = self.adult_stoke
        cols1 = ['성별', '고혈압', '심장병', '기혼여부', '직종', '거주형태', '흡연여부']
        print(t[cols1].dtypes)
        print(t[cols1].isnull().sum()) # 결측 값
        print(f'--- 결측값 있는 변수 --- \n {t[cols1].isna().any()[lambda x: x]}')
        # 결측값 x
        t['성별'] = OrdinalEncoder().fit_transform(t['성별'].values.reshape(-1, 1))
        t['기혼여부'] = OrdinalEncoder().fit_transform(t['기혼여부'].values.reshape(-1, 1))
        t['직종'] = OrdinalEncoder().fit_transform(t['직종'].values.reshape(-1, 1))
        t['거주형태'] = OrdinalEncoder().fit_transform(t['거주형태'].values.reshape(-1, 1))
        t['흡연여부'] = OrdinalEncoder().fit_transform(t['흡연여부'].values.reshape(-1, 1))

        self.adult_stoke.to_csv('C:/Users/bitcamp/PycharmProjects/flaskProject/static/save/dam/ml/stroke.csv')

    def ordinal_variables(self):
        pass

    '''
        데이터프레임을 데이터 파티션하기 전에 타깃변수와 입력변수를 
        target 과 data 에 분리하여 저장한다.
    '''

    def target(self):
        df = pd.read_csv('../../../../static/save/dam/ml/stroke.csv')
        self.data = df.drop(['뇌졸중'], axis=1)
        self.target = df['뇌졸중']
        print(f'--- data shape\n {self.data}' )
        print(f'--- targe shape\n{self.target}')

    def partition(self):
        dframe = pd.read_csv('../../../../static/save/dam/ml/stroke.csv')
        data = dframe.drop(['뇌졸중'], axis=1)
        target = dframe['뇌졸중']
        undersample = RandomUnderSampler(sampling_strategy=0.333, random_state= 2)
        data_under, target_under = undersample.fit_resample(data, target)
        print(target_under.value_counts(dropna=True))
        # 50 : 50 데이터 분할
        X_train, X_test, y_train, y_test = train_test_split(data_under, target_under, test_size=0.5, random_state=42, stratify=target_under)
        print("X_train shape:", X_train.shape)
        print("X_test shape:", X_test.shape)
        print("y_train shape:", y_train.shape)
        print("y_test shape:", y_test.shape)
        print(y_train.value_counts(normalize=True)) # %
        print(y_train.value_counts())



