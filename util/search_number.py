from randomlist import Randomlist
from util.common import Common


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
            menu = Common.menu()
            if menu == 1 :
                print("### 배수 등록 ###")
                ls.append(SearchNumber.new_menu())
            elif menu == 2 :
                print("### 배수 목록 ###")
                SearchNumber.get_searchNumber(ls)
            elif menu == 3 :
                print("### 배수 삭제 ###")
                SearchNumber.delete_searchNumber(ls, int(input("삭제 할 배수 :")))
            elif menu == 4 :
                print("### 배수 등록 ###")
            else: print("### 종료 ###")

SearchNumber.main()