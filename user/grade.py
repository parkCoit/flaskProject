from util.common import Common


class Grade(object):
    def __init__(self, name, ko, en, ma):
        self.name= name
        self.ko = ko
        self.en = en
        self.ma = ma
        self.total = ko + en + ma
        self.va = self.total / 3

    def get_grade(self):
        va = self.va
        grade = ""
        if va >= 90:
            grade = "A 학점"
        elif va >= 80:
            grade = "B 학점"
        elif va >= 70:
            grade = "C 학점"
        elif va >= 60:
            grade = "D 학점"
        elif va >= 50:
            grade = "E 학점"
        else: grade = "F 학점"
        return grade

    def __str__(self):
        return f" {self.name} {self.ko} {self.en} {self.ko} {self.total} {self.va} {self.get_grade()} "

    @staticmethod
    def new_grade():
        return Grade(input("이름 :"),
                     int(input("국어 :")),
                     int(input("영어 :")),
                     int(input("수학 :")))

    @staticmethod
    def get_grades(ls):
        [print(i) for i in ls ]

    @staticmethod
    def delete_grade(ls, name):
        del ls[[i for i, j in enumerate(ls) if j.name == name][0]]

