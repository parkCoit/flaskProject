class Common(object):
    def __init__(self):
        pass

    @staticmethod
    def menu(ls):
        for i, j in enumerate(ls): # ["종료", "등록", "목록", "삭제"]
            print(f"{i}. {j}")
        return input("메뉴 :")