from auth.user import Member
from util.common import Common

ls = []
while True:
    menu = Common.menu(["종료", "회원 가입"])
    if menu == 0 :
        print("### 종료 ###")
        break
    elif menu == 1 :
        while True:
            submenu = Common.menu(["종료", "회원 가입", "가입 목록", "가입 탈퇴"])
            if submenu == 0:
                break
            elif submenu == 1:
                ls.append(Member.new_member())
            elif submenu == 2:
                Member.get_member(ls)
            elif submenu == 3:
                Member.delete_member(ls, input("아이디 :"))
            else:
                print(" 잘못된 값 ")
