from src.cmm.service.common import Common


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