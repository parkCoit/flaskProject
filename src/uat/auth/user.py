class Member(object):
    def __init__(self, id, pw, name):
        self.id = id
        self.pw = pw
        self.name = name

    def __str__(self):
        return f"{self.id} {self.pw} {self.name} "

    @staticmethod
    def new_member():
        return Member(input(" 아이디 : "),
                      input(" 비밀번호 : "),
                      input(" 이름 : "))

    @staticmethod
    def get_member(ls):
        [print(i) for i in ls]

    @staticmethod
    def delete_member(ls, id):
         del ls[[ i if j.id == id else print("no") for i, j in enumerate(ls) ][0]]