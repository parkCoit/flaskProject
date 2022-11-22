from src.dam.bicycle.service.model import BicycleModel
from src.dam.bicycle.service.view import BicycleController
from src.cmm.service.common import Common



api = BicycleController()
model = BicycleModel()

while True:
    menu = Common.menu(["종료", "시각화", "모델링", "머신 러닝", "배포"])
    if menu =="0" :
        print("### 종료 ###")
        break
    elif menu == "1" :
        print("### 시각화 ###")
        print(BicycleModel())
        #hour_bef_temperature        2
        #hour_bef_precipitation      2
        #hour_bef_windspeed          9
        #hour_bef_humidity           2
        #hour_bef_visibility         2
        #hour_bef_ozone             76
        #hour_bef_pm10              90
        #hour_bef_pm2.5            117
    elif menu == "2" :
        print("### 모델링 ###")
    elif menu == "3" :
        print("### 머신 러닝 ###")
    elif menu == "4" :
        print("### 배포 ###")
    else : print("해당 메뉴 없음")