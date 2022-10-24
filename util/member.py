class Member(object):
    def __init__(self, id, pw, name):
        self.id = id
        self.pw = pw
        self.name = name

    def print_member(self):
        print(f"{self.id} {self.pw} {self.name} ")

    @staticmethod
    def print_menu():
        print("1. 회원 가입")
        print("2. 목록")
        print("3. 탈퇴")
        print("4. 종료")
        return int(input("메뉴 선택 :"))

    @staticmethod
    def new_member():
        id = input(" 아이디 : ")
        pw = input(" 비밀번호 : ")
        name = input(" 이름 : ")
        return Member(id, pw, name)

    @staticmethod
    def get_member(ls):
        [i.print_member() for i in ls]

    @staticmethod
    def delete_member(ls, id):
         del ls[[ i if j.id == id else print("no") for i, j in enumerate(ls) ][0]]



    @staticmethod
    def main():
        ls = []
        while True :
            menu = Member.print_menu()
            if menu == 1 :
                print("### 회원 가입 ###")
                ls.append(Member.new_member())
            elif menu == 2:
                print("### 목록 ###")
                Member.get_member(ls)
            elif menu == 3 :
                print("### 탈퇴 ###")
                Member.delete_member(ls, input("아이디 :"))
            elif menu == 4 :
                print("### 종료 ###")
                break
            else :
                print(" 잘못된 값 ")


Member.main()