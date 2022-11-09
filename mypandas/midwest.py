import pandas as pd

midwest = pd.read_csv("./data/midwest.csv")
menus = ["종료",
             "메타데이터 출력",
             "poptotal/popasian 변수를 total/asian로 이름변경",
             "전체 인구 대비 아시아 인구 백분율 변수 추가",
             "아시아 인구 백분율 전체 평균을 large/small 로 분류",
             "large/small 빈도표와 빈도막대그래프 작성"]
while True:
    for i,j in enumerate(menus):
        print(f"{i}. {j}")

    menu = input("메뉴 :")
    if menu == "0":
        print(menus[0])
        break
    elif menu =="1":
        print(menus[1])
        print(midwest.info())
    elif menu =="2":
        print(menus[2])
    elif menu =="3":
        print(menus[3])
    elif menu =="4":
        print(menus[4])
    elif menu =="5":
        print(menus[5])
    else : print("잘못 된 값")