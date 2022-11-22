from string import ascii_lowercase

import numpy as np
import pandas as pd


def new_friuts_df():
    name = ["제품", "가격", "판매량"]
    ls2 = ["사과", "딸기", "수박"]
    ls3 = [1800, 1500, 3000]
    ls4 = [30,40,50]
    a = [ls2,ls3,ls4]

    dc = {}
    for i, j in enumerate(name):
       dc[j] = a[i] # dc 는 key 값 가져옴 a[i]는 a의 인덱스 값 i 설정
    #dc = {j : a[i]for i, j in enumerate(name)}
    print(dc)
    df = pd.DataFrame.from_dict(dc)
    #df = pd.DataFrame(dc)
    print(df)
    print(sum(df["가격"])//3)
    print(sum(df["판매량"])//3)

def new_number_2d():
    a = range(1,10)
    print(a)
    df = pd.DataFrame(np.array([list(range(1, 11)),
                                list(range(11, 21)),
                                list(range(21, 31))]),
                      #columns=["a","b","c","d","e","f","g","h","i","j"]
                      columns=list(ascii_lowercase)[0:10]) # lower 소문자 upper 대문자
    print(df)





if __name__ == '__main__':
    menus = ["종료", "과일2D", "숫자2D"]
    while True :
        menu =[print(f"{i}.{j}") for i, j in enumerate(menus)]
        num = input("메뉴 :")
        if num == "0":
            print(menus[0])
            break
        elif num == "1":
            print(menus[1])
            new_friuts_df()
        elif num == "2":
            print(menus[2])
            new_number_2d()

