from mypandas.fruits import Fruits
from util.common import Common

ls = []
while True:
    menu = Common.menu(["종료", "과일 등록"])
    if menu == 0 :
        print("### 종료 ###")
        break
    elif menu == 1 :
        while True :
            submenu = Common.menu(["종료", "과일 등록", "과일 목록", "과일 삭제"])
            if submenu == 0:
                break
            elif submenu == 1:
                ls.append(Fruits.new_menu())
            elif submenu == 2:
                Fruits.get_fruits(ls)
            elif submenu == 3:
                Fruits.delete_fruit(ls, input("과일 이름:"))
            else: print("잘못 된 값")