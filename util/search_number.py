from randomlist import Randomlist

class SearchNumber(object):
    def __init__(self, num ):
        self.num = num

    def print_searchNumber(self):
        rl1 = Randomlist().get_random(10 , 100 , 10)
        print(f"배수 : {self.num} \n 나온 값: {rl1} ")
        for i in rl1:
            if i %  self.num == 0:
                print(f"{self.num}배수 의 값 : {i}")

    @staticmethod
    def print_menu():
        print("1. 배수 등록")
        print("2. 배수 목록")
        print("3. 배수 삭제")
        print("4. 종료")
        return int(input("메뉴 :"))

    @staticmethod
    def new_menu():
        return SearchNumber(int(input("배수 :")))

    @staticmethod
    def get_searchNumber(ls):
        [i.print_searchNumber() for i in ls]

    @staticmethod
    def delete_searchNumber(ls, num):
        del ls[[i for i,j in enumerate(ls) if j.num == num][0]]


    @staticmethod
    def main():
        ls = []
        while True:
            menu = SearchNumber.print_menu()
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