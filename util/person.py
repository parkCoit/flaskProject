class Person:
    def __init__(self, name, ssn, juso) -> None:
        self.name = name
        self.ssn = ssn
        self.juso = juso
        self.age = 0
        self.gender = ""

    def print_person(self):
        current = 2022
        year = int(self.ssn[:2])
        gender_checker = int(self.ssn[7])
        if gender_checker == 1 or gender_checker == 2:
            year += 1900
            if gender_checker == 1:
                self.gender = "남성"
            else:
                self.gender = "여성"
        elif gender_checker == 3 or gender_checker == 4:
            year += 2000
            if gender_checker == 3:
                self.gender = "남성"
            else:
                self.gender = "여성"
        self.age = current - year

        print(f"{self.name} {self.age} {self.gender} {self.juso} ")

    @staticmethod
    def print_menu():
        print("1. 신원 등록")
        print("2. 신원 정보")
        print("3. 신원 삭제")
        print("4. 종료")
        return int(input("메뉴 :"))

    @staticmethod
    def new_person():
        name = input("이름 : ")
        ssn = input("주민번호 : ")
        juso = input("주소 : ")
        return Person(name, ssn, juso)

    @staticmethod
    def get_person(ls):
        [i.print_person() for i in ls]

    @staticmethod
    def delete_person(ls, ssn):
        del ls[[i for i, j in enumerate(ls) if j.ssn == ssn][0]]


    @staticmethod
    def main():
        ls = []
        while True :
            menu = Person.print_menu()
            if menu == 1:
                print("신원 등록 ")
                ls.append(Person.new_person())
            elif menu == 2:
                print("신원 정보 ")
                Person.get_person(ls)
            elif menu == 3:
                print("신원 삭제 ")
                Person.delete_person(ls, input("주민번호"))
            elif menu == 4:
                print("종료 ")
                break
            else: print("잘못 된 값")

Person.main()