from randomlist import Randomlist
from src.cmm.service.common import Common


class SearchNumber(object):
    def __init__(self, num ):
        self.num = num

    def __str__(self):
        rl1 = Randomlist().get_random(10 , 100 , 10)
        print(f"배수 : {self.num} \n 나온 값: {rl1} ")
        for i in rl1:
            if i %  self.num == 0:
                return f"{self.num}배수 의 값 : {i}"

    @staticmethod
    def new_menu():
        return SearchNumber(int(input("배수 :")))

    @staticmethod
    def get_searchNumber(ls):
        [print(i) for i in ls]

    @staticmethod
    def delete_searchNumber(ls, num):
        del ls[[i for i,j in enumerate(ls) if j.num == num][0]]


    @staticmethod
    def main():
        ls = []
        while True:
            menu = Common.menu(ls)
            if menu == "0" :
                print("### 종료 ###")
                break
            if menu == "1" :
                print("### 배수 등록 ###")
                ls.append(SearchNumber.new_menu())
            elif menu == "2" :
                print("### 배수 목록 ###")
                SearchNumber.get_searchNumber(ls)
            elif menu == "3" :
                print("### 배수 삭제 ###")
                SearchNumber.delete_searchNumber(ls, int(input("삭제 할 배수 :")))
            else: print("### 잘못 된 값 ###")

SearchNumber.main()
"""
if __name__ == '__main__':
    ls = []

    person_menus = ["종료", "신원 등록", "신원 정보", "신원 삭제"]

    person_menu = {
        "1": lambda t: ls.append(t.new_person()),
        "2": lambda t: t.get_person(ls),
        "3": lambda t: t.delete_person(ls, input("주민번호"))

    }

    if __name__ == '__main__':

        t = Person
        while True:
            [print(f"{i}. {j}") for i, j in enumerate(person_menus)]
            menu = input('메뉴선택: ')
            if menu == '0':
                print("종료")
                break
            else:
                try:
                    person_menu[menu](t)

                except KeyError:
                    print(" ### Error ### ")
"""