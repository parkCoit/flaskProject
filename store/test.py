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


if __name__ == '__main__':
    new_friuts_df()