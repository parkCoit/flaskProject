class Calculator(object):
    def __init__(self, num1, op, num2):
        self.num1 = num1
        self.op = op
        self.num2 = num2

    def print_calculator(self): # def Method, self 객체 자신을 의미
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
        print(f"{num1} {op} {num2}  = {result}")

    @staticmethod
    def print_menu():
        print("1. 입력")
        print("2. 출력")
        print("3. 삭제")
        print("4. 종료")

    @staticmethod
    def new_calculator():
        num1 = int(input("숫자 : "))
        op = input("연산자 : ")
        num2 = int(input("숫자 : "))
        return Calculator(num1, op, num2)

    @staticmethod
    def get_calculator(ls):
        [i.print_calculator() for i in ls]

    @staticmethod
    def delete_calculator(ls, op):
        del ls[[i for i, j in enumerate(ls) if j.op == op][0]]

    @staticmethod
    def main():
        def main():
            ls = []
            while True :
                menu = Calculator.print_menu()
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