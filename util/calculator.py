from util.common import Common


class Calculator(object):
    def __init__(self, num1, op, num2):
        self.num1 = num1
        self.op = op
        self.num2 = num2

    def __str__(self):
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
        return f"{num1} {op} {num2}  = {result}"

    @staticmethod
    def new_calculator():
        num1 = int(input("숫자 : "))
        op = input("연산자 : ")
        num2 = int(input("숫자 : "))
        return Calculator(num1, op, num2)

    @staticmethod
    def get_calculator(ls):
        [print(i) for i in ls]

    @staticmethod
    def delete_calculator(ls, op):
        del ls[[i for i, j in enumerate(ls) if j.op == op][0]]

    @staticmethod
    def main():
        ls = []
        while True :
            menu = Common.menu()
            if menu == 1:
                print("### 입력 ###")
                ls.append(Calculator.new_calculator())
            elif menu == 2:
                print("### 출력 ###")
                Calculator.get_calculator(ls)
            elif menu == 3:
                print("### 삭제 ###")
                Calculator.delete_calculator(ls, input("기호 :"))
            elif menu == 4:
                print("### 종료 ###")
                break
            else : print("잘못 된 값")

Calculator.main()