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

    def print_grade(self):
        print(f" {self.name} {self.ko} {self.en} {self.ko} {self.total} {self.va} {self.get_grade()} ")


    @staticmethod
    def print_menu():
        print("1. 성적 등록")
        print("2. 성적표")
        print("3. 성적 삭제")
        print("4. 종료")
        return  int(input("메뉴 :"))

    @staticmethod
    def new_grade():
        name = input("이름 :")
        ko = int(input("국어 :"))
        en = int(input("영어 :"))
        ma = int(input("수학 :"))
        return Grade(name, ko, en, ma)

    @staticmethod
    def get_grades(ls):
        [i.print_grade() for i in ls ]

    @staticmethod
    def delete_grade(ls, name):
        del ls[[i for i, j in enumerate(ls) if j.name == name][0]]


    @staticmethod
    def main():
        ls = []
        while True :
            menu = Grade.print_menu()
            if menu == 1 :
                print("### 성적 등록 ###")
                ls.append(Grade.new_grade())
            elif menu == 2 :
                print("### 성적표 ###")
                Grade.get_grades(ls)
            elif menu == 3 :
                print("### 성적 삭제 ###")
                Grade.delete_grade(ls, input("이름 :"))
            elif menu == 4 :
                print("### 종료 ###")
                break
            else : print("잘못 된 값")

Grade.main()