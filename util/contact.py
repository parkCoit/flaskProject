class Contact(object):
    def __init__(self, name, num, mail, adr):
        self.name = name
        self.num = num
        self.mail = mail
        self.adr = adr

    def print_info(self):
        print(f"{self.name} {self.num} {self.mail} {self.adr}")



    @staticmethod
    def print_menu():
        print("1. 연락처 등록")
        print("2. 연락처 목록")
        print("3. 연락처 삭제")
        return int(input("메뉴 :"))

    @staticmethod
    def new_contact():
        name = input("이름 :")
        num = input("전화 번호 :")
        mail = input("이메일 :")
        adr = input("주소 :")
        return Contact(name, num, mail, adr)

    @staticmethod
    def print_contacts(ls):
        [i.print_info() for i in ls]


    @staticmethod
    def delete_contact(ls, name):
        del ls[[i for i, j in enumerate(ls) if j.name == name][0]]



    @staticmethod
    def main():
        ls = []
        while True:
            menu = Contact.print_menu()
            if menu == 1:
                print(" ### 연락처 등록 ###")
                ls.append(Contact.new_contact())
            elif menu == 2:
                print(" ### 연락처 목록 ###")
                Contact.print_contacts(ls)
            elif menu == 3:
                print(" ### 연락처 삭제 ###")
                Contact.delete_contact(ls, input(" 이름: "))
            elif menu == 4:
                print(" 주소록 어플을 종료 합니다 ")
                break
            else : print("잘못된 값")

Contact.main()