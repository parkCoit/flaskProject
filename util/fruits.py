class Fruits(object):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def print_fruit(self):
        print(f"{self.name} {self.price}")


    @staticmethod
    def print_menu():
        print("1. 과일 등록")
        print("2. 과일 목록")
        print("3. 과일 삭제")
        print("4. 종료")
        return int(input("메뉴 :"))

    @staticmethod
    def new_menu():
        return Fruits(input("과일 이름 :"), input("가격 :"))

    @staticmethod
    def get_fruits(ls):
        for i in ls :
            i.print_fruit()

    @staticmethod
    def delete_fruit(ls, name):
        del ls[[i for i, j in enumerate(ls) if j.name == name][0]]

    @staticmethod
    def main():
        ls = []
        while True :
            menu = Fruits.print_menu()
            if menu == 1:
                print("### 과일 등록 ###")
                ls.append(Fruits.new_menu())
            elif menu == 2:
                print("### 과일 목록 ###")
                Fruits.get_fruits(ls)
            elif menu == 3:
                print("### 과일 삭제 ###")
                Fruits.delete_fruit(ls, input("과일 이름:"))
            elif menu == 4:
                print("### 과일 등록 ###")
            else: print("잘못 된 값")

Fruits.main()