import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

from titanic.template import Plot
from titanic.views import TitanicController
from util.common import Common


if __name__ == '__main__':  # 두번도는거 막기
    api = TitanicController()

    while True:
        menu = Common.menu(["종료", "시각화", "모델링", "머신 러닝", "배포"])
        if menu == "0":
            print("### 종료 ###")
            break
        elif menu == "1":
            print("### 시각화 ###")
            train = Plot("train.csv")
            train.draw_survived()
            train.draw_pclass()
            train.draw_sex()

        elif menu == "2":
            print("### 모델링 ###")
        elif menu == "3":
            print("### 머신 러닝 ###")
        elif menu == "4":
            print("### 배포 ###")
        else:
            print("해당 메뉴 없음")