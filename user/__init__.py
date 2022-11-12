from user.bmi import Bmi
from user.contact import Contact
from user.grade import Grade
from user.person import Person
from util.common import Common

ls = []
while True:
    menu = Common.menu(["종료","BMI 등록","연락처 등록", "성적 등록", "신원 등록"])
    if menu == 0:
        print("### 앱 종료 ###")
        break

    elif menu == 1:
        while True:
            print("### BMI ###")
            submenu = Common.menu(["종료", "BMI 등록", "BMI 목록", "BMI 삭제"])
            if submenu == 0:
                break
            elif submenu == 1:
                ls.append(Bmi.new_bmi())
            elif submenu == 2:
                Bmi.get_bmis(ls)
            elif submenu == 3:
                Bmi.delete_bmi(ls, input("이름 :"))
            else:
                print("잘못 된 값")

    elif menu == 2:
        while True:
            print("### 연락처 ###")
            submenu = Common.menu(["종료", "연락처 등록", "연락처 목록", "연락처 삭제"])
            if submenu == 0:
                break
            elif submenu == 1:
                ls.append(Contact.new_contact())
            elif submenu == 2:
                Contact.print_contacts(ls)
            elif submenu == 3:
                Contact.delete_contact(ls, input(" 이름: "))
            else:
                print("잘못 된 값")

    elif menu == 3:
        while True :
            print("### 성적표 ###")
            submenu = Common.menu(["종료", "성적표 등록", "성적표 목록", "성적표 삭제"])
            if submenu == 0:
                break
            elif submenu == 1:
                ls.append(Grade.new_grade())
            elif submenu == 2:
                Grade.get_grades(ls)
            elif submenu == 3:
                Grade.delete_grade(ls, input("이름 :"))
            else:
                print("잘못 된 값")

    elif menu == 4:
        while True :
            print("### 개인 정보 ###")
            submenu = Common.menu(["종료", "개인정보 등록", "개인정보 목록", "개인정보 삭제"])
            if submenu == 0:
                break
            elif submenu == 1:
                ls.append(Person.new_person())
            elif submenu == 2:
                Person.get_person(ls)
            elif submenu == 3:
                Person.delete_person(ls, input("주민번호"))
            else:
                print("잘못 된 값")
