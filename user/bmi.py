from util.common import Common
class Bmi(object):
    def __init__(self, name, cm, kg):
        self.name = name
        self.cm = cm
        self.kg = kg
        self.bmi = kg / (self.cm/100) ** 2

    def __str__(self):
        return f"{self.name} {self.cm} {self.kg} {self.set_biman()} "

    def set_biman(self):
        biman = ""
        bmi = self.bmi
        if (bmi >= 35):
            biman = "고도비만"
        elif (bmi >= 25):
            biman = "중도비만"
        elif (bmi >= 23):
            biman = "과체중"
        elif (bmi >= 18.5):
            biman = "정상"
        else:
            biman = "저체중"
        return biman


    @staticmethod
    def new_bmi():
        return Bmi(input("이름 :"),
                   int(input("키 :")),
                   int(input("몸무게 :")))

    @staticmethod
    def get_bmis(ls):
        [print(i) for i in ls]


    @staticmethod
    def delete_bmi(ls, name):
        del ls[[i for i,j in enumerate(ls) if j.name == name][0]]


