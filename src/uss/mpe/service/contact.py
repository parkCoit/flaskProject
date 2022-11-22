class Contact(object):
    def __init__(self, name, num, mail, adr):
        self.name = name
        self.num = num
        self.mail = mail
        self.adr = adr

    def __str__(self):
        return f"{self.name} {self.num} {self.mail} {self.adr}"

    @staticmethod
    def new_contact():
        return Contact(input("이름 :"),
                       input("전화 번호 :"),
                       input("이메일 :"),
                       input("주소 :"))

    @staticmethod
    def print_contacts(ls):
        [print(i) for i in ls]


    @staticmethod
    def delete_contact(ls, name):
        del ls[[i for i, j in enumerate(ls) if j.name == name][0]]



