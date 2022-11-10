import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

midwest = pd.read_csv("./data/midwest.csv")






menus = ["종료",
             "메타데이터 출력",
             "poptotal/popasian 변수를 total/asian로 이름변경",
             "전체 인구 대비 아시아 인구 백분율 변수 추가",
             "아시아 인구 백분율 전체 평균을 large/small 로 분류",
             "large/small 빈도표와 빈도막대그래프 작성"]


class MidWest:
    def __init__(self):
        self.midwest = pd.read_csv("./data/midwest.csv")
        self.midwest_add_test = None

    def name_change(self):
        self.midwest_add_test = self.midwest.rename(columns={"poptotal":'total', "popasian" : 'asian'})
        print(self.midwest_add_test.columns)
    def pct_hist(self):
        self.name_change()
        mw = self.midwest_add_test
        mw['pct'] = (mw['asian'] / mw['total']) * 100
        mw['pct'].plot.hist()
        plt.savefig('./save/midwest_hist.png')

    def asia_large_small(self):
        self.pct_hist()
        mw = self.midwest_add_test
        avg = mw['pct'].mean()
        mw['pct'] = np.where(mw['pct'] > avg, "large", "small")
        print(mw['pct'])

    def var_large_small(self):
        self.asia_large_small()
        mw =self.midwest_add_test
        count_grade = mw['pct'].value_counts()
        print(count_grade)
        count_grade.plot.bar(rot = 0)
        plt.savefig('./save/midwest_var.png')


if __name__ == '__main__':
    MW = MidWest()

    while True:
        for i,j in enumerate(menus):
            print(f"{i}. {j}")

        menu = input("메뉴 :")
        if menu == "0":
            print(menus[0])
            break
        elif menu =="1":
            print(menus[1])
            print(midwest)
        elif menu =="2":
            print(menus[2])
            MW.name_change()
        elif menu =="3":
            print(menus[3])
            MW.pct_hist()
        elif menu =="4":
            print(menus[4])
            MW.asia_large_small()
        elif menu =="5":
            print(menus[5])
            MW.var_large_small()
        else : print("잘못 된 값")