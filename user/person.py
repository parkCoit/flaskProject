from util.common import Common


class Person:
    def __init__(self, name, ssn, juso) -> None:
        self.name = name
        self.ssn = ssn
        self.juso = juso
        self.age = 0
        self.gender = ""

    def __str__(self):
        current = 2022
        year = int(self.ssn[:2]) # 인덱스 0, 1은 출생년도
        gender_checker = int(self.ssn[7]) # 7은 성별판별번호 인덱스
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

        return f"{self.name} {self.age} {self.gender} {self.juso} "

    @staticmethod
    def new_person():
        return Person(input("이름 : "),
                      input("주민번호 : "),
                      input("주소 : "))

    @staticmethod
    def get_person(ls):
        [print(i) for i in ls]

    @staticmethod
    def delete_person(ls, ssn):
        del ls[[i for i, j in enumerate(ls) if j.ssn == ssn][0]]

