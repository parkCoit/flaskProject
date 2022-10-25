from util.common import Common


class Fruits(object):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} {self.price}"

    @staticmethod
    def new_menu():
        return Fruits(input("과일 이름 :"), input("가격 :"))

    @staticmethod
    def get_fruits(ls):
        [print(i) for i in ls]


    @staticmethod
    def delete_fruit(ls, name):
        del ls[[i for i, j in enumerate(ls) if j.name == name][0]]
