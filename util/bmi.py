
class Bmi(object):
    def __init__(self, name, cm, kg):
        self.name = name
        self.cm = cm
        self.kg = kg

    def get_bmi(self):
        kg = self.kg
        m = self.cm / 100
        return kg / m ** 2

    def print_biman(self):
        biman = ""
        bmi = self.get_bmi()
        if(bmi >= 35) : biman = "고도비만"
        elif(bmi >= 25) : biman ="중도비만"
        elif(bmi >= 23) : biman = "과체중"
        elif(bmi >= 18.5) : biman = "정상"
        else: biman = "저체중"
        print(f"{self.name} {self.cm} {self.kg} {biman} ")


    @staticmethod
    def new_bmi():
        name = input("이름 :")
        cm = int(input("키 :"))
        kg = int(input("몸무게 :"))
        return Bmi(name, cm, kg)

    @staticmethod
    def print_menu():
        print("1. 등록 ")
        print("2. 목록 ")
        print("3. 삭제 ")
        return int(input("메뉴 :"))

    @staticmethod
    def get_bmis(ls):
        [i.print_biman() for i in ls]


    @staticmethod
    def delete_bmi(ls, name):
        del ls[[i for i,j in enumerate(ls) if j.name == name][0]]

    @staticmethod
    def main():
        ls = []
        while True :
            menu = Bmi.print_menu()
            if menu == 1 :
                print("### 등록 ###")
                ls.append(Bmi.new_bmi())
            elif menu == 2 :
                print("### 목록 ###")
                Bmi.get_bmis(ls)
            elif menu == 3 :
                print("### 삭제 ###")
                Bmi.delete_bmi(ls, input("이름 :"))
            elif menu == 4 :
                print("### 종료 ###")
                break
            else : print("잘못 된 값")



Bmi.main()