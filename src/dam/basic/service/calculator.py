from src.cmm.service.common import Common


class Calculator(object):
    def __init__(self, num1, op, num2):
        self.num1 = num1
        self.op = op
        self.num2 = num2
        self.result = self.get_result()

    def __str__(self):
        return f"{self.num1} {self.op} {self.num2}  = {self.result}"

    def get_result(self):
        num1 = self.num1
        op = self.op
        num2 = self.num2
        if self.op == "+":
            result = num1 + num2
        elif self.op == "-":
            result = num1 - num2
        elif self.op == "*":
            result = num1 * num2
        elif self.op == "/":
            result = num1 / num2
        elif self.op == "%":
            result = num1 % num2
        else :
            result = "잘못된 연산자 입니다."
        return result

    @staticmethod
    def new_calculator():
        num1 = int(input("처음 수 : "))
        op = input("연산자 : ")
        num2 = int(input("두번 째 수 : "))
        return Calculator(num1, op, num2)

    @staticmethod
    def get_calculator(ls):
        [print(i) for i in ls]

    @staticmethod
    def delete_calculator(ls, op):
        del ls[[i for i, j in enumerate(ls) if j.op == op][0]]



ls = []

calculator_menus = ["종료", "입력", "출력", "삭제"]

calculator_menu = {
    "1": lambda t: ls.append(t.new_calculator()),
    "2": lambda t: t.get_calculator(ls),
    "3": lambda t: t.delete_calculator(ls, input("기호 :"))

        }

if __name__ == '__main__':

    t = Calculator
    while True:
        [print(f"{i}. {j}") for i, j in enumerate(calculator_menus)]
        menu = input('메뉴선택: ')
        if menu == '0':
            print("종료")
            break
        else:
            try:
                calculator_menu[menu](t)

            except KeyError:
                print(" ### Error ### ")



