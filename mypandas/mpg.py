import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

"""
RangeIndex: 234 entries, 0 to 233
Data columns (total 12 columns):
 #   Column        Non-Null Count  Dtype  
---  ------        --------------  -----  
 0   Unnamed: 0    234 non-null    int64   
 1   manufacturer  234 non-null    object   / 회사
 2   model         234 non-null    object   / 모델
 3   displ         234 non-null    float64  / 베기량
 4   year          234 non-null    int64    / 연식
 5   cyl           234 non-null    int64    / 실린더
 6   trans         234 non-null    object   / 차축
 7   drv           234 non-null    object   / 오토
 8   cty           234 non-null    int64    / 시내연비
 9   hwy           234 non-null    int64    / 시외연비
 10  fl            234 non-null    object   / 연료
 11  class         234 non-null    object   / 차종
dtypes: float64(1), int64(5), object(6)
memory usage: 22.1+ KB
"""


my_meta = {
    "manufacturer" : "회사",
    "model" : "모델",
    "displ" : "베기량",
    "year" : "연식",
    "cyl" : "실린더",
    "trans" : "차축",
    "drv" : "오토",
    "cty" : "시내연비",
    "hwy" : "시외연비",
    "fl" : "연료",
    "class" : "차종"
}

class Mypandas(object):

    def __init__(self):
        self.mpg = pd.read_csv("./data/mpg.csv")
        self.mpg_add_test = None

    def head(self):
        print(self.mpg.head(3))

    def tail(self):
        print(self.mpg.tail(3))

    def shape(self):
        print(self.mpg.shape)

    def info(self):
        print(self.mpg.info())

    def describe(self):
        print(self.mpg.describe())

    def describe_include(self):
        print(self.mpg.describe(include='all'))

    def change_meta(self):
        self.mpg_add_test = self.mpg.rename(columns=my_meta)

    def var_test(self):
        self.change_meta()
        mpg = self.mpg_add_test
        mpg["총연비"] = (mpg['시내연비'] + mpg['시외연비']) / 2
        mpg["연비테스트"] = np.where(mpg['총연비'] >= 20, 'pass', 'fail')
        self.mpg_add_test = mpg


    def value_count_test(self):
        self.var_test()
        mpg = self.mpg_add_test
        self.count_test = mpg['연비테스트'].value_counts()


    def create_bar_test(self):
        self.value_count_test()
        self.count_test.plot.bar(rot=0)
        plt.savefig('./save/draw_freq_bar_graph.png')

    def compare_hwy(self):
        self.change_meta()
        mpg = self.mpg_add_test
        a = mpg.query("베기량 < 4")
        b = mpg.query("베기량 > 5")
        c = a['시외연비'].mean()
        d = b['시외연비'].mean()
        self.mpg_add_test = mpg
        print(c)
        print(d)
    """
    def company_cty(self):
        self.compare_hwy()
        mpg = self.mpg_add_test
        print(mpg)
        a = mpg.query("회사" == "audi")
        b = mpg.query("회사" == "toyota")
        c = a["도시연비"].mean()
        d = b["도시연비"].mean()
        print(c)
        print(d)
    """




if __name__ == '__main__':

    m = Mypandas()
    while True:
        menus = ["종료",
                 "mpg 앞부분 확인",
                 "mpg 뒷부분 확인",
                 "행,열 출력",
                 "데이터 속성 확인",
                 "요약 통계량 출력",
                 "문자 변수 요약 통계량 함께 출력",
                 "manufacturer 를 company로 변경",
                 "test 변수 생성",
                 #"cty 와 hwy 변수를 머지(merge)하여 total 변수 생성하고 20이상이면 pass 미만이면 fail 저장"
                 "test 빈도표 만들기",
                 "test 빈도 막대 그래프 그리기",
                 # mpg 144페이지 문제
                 "displ(배기량)이 4이하와 5이상 자동차의 hwy(고속도로 연비) 비교",
                 "아우디와 토요타 중 도시연비(cty) 평균이 높은 회사 검색",
                 "쉐보레, 포드, 혼다 데이터 출력과 hwy 전체 평균"
                 # mpg 150페이지 문제
                 # 메타데이터가 category, cty 데이터는 해당 raw 데이터인 객체생성
                 # 후 다음 문제 풀이
                 "suv / 컴팩 자동차 중 어떤 자동차의 도시연비 평균이 더 높은가?"
                 # mpg 153페이지 문제
                 "아우디차에서 고속도로 연비 1~5위 출력하시오"
                 # mpg 158페이지 문제
                 "평균연비가 가장 높은 자동차 1~3위 출력하시오"
                 ]

        for i, j in enumerate(menus):
            print(f"{i}. {j}")

        menu = input("메뉴 :")

        if menu == "0":
            print(menus[0])
            break
        elif menu =="1":
            print(menus[1])
            m.head()
        elif menu =="2":
            print(menus[2])
            m.tail()
        elif menu =="3":
            print(menus[3])
            m.shape()
        elif menu =="4":
            print(menus[4])
            m.info()
        elif menu =="5":
            print(menus[5])
            m.describe()
        elif menu =="6":
            print(menus[6])
            m.describe_include()
        elif menu =="7":
            print("manufacturer 를 company로 변경")
            m.change_meta()
        elif menu == "8":
            print("test 변수 생성")
            m.var_test()
        elif menu == "9":
            print("test 빈도표 만들기")
            m.value_count_test()
        elif menu == "10":
            print("test 빈도 막대 그래프 그리기")
            m.create_bar_test()
        elif menu == "11":
            print("displ(배기량)이 4이하와 5이상 자동차의 hwy(고속도로 연비) 비교")
            m.compare_hwy()
        elif menu == "12":
            print("아우디와 토요타 중 도시연비(cty) 평균이 높은 회사 검색")
            m.company_cty()
        elif menu == "13":
            print("쉐보레, 포드, 혼다 데이터 출력과 hwy 전체 평균")
        elif menu == "14":
            print("suv / 컴팩 자동차 중 어떤 자동차의 도시연비 평균이 더 높은가?")
        elif menu == "15":
            print("아우디차에서 고속도로 연비 1~5위 출력하시오")
        elif menu == "16":
            print("평균연비가 가장 높은 자동차 1~3위 출력하시오")

        else : print("잘못 된 값")
