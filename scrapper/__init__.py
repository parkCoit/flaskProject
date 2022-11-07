from scrapper.domains import MusicRanking
from scrapper.views import ScrapperController
from util.common import Common

api = ScrapperController()
if __name__ == '__main__':
    m = MusicRanking()
    while True :
        menus = ["종료", "벅스뮤직", "멜론뮤직"]
        menu = Common.menu(menus)
        if menu == "0":
            print(menus[0])
            break
        elif menu == "1":
            print(menus[1])
            m.domain ="https://music.bugs.co.kr/chart/track/day/total?chartdate="
            m.query_string = "20221101"
            m.parser = "lxml"
            m.class_names= "title"
            m.class_names= "artist"
            m.tag_name = "p"
            api.menu_1(m)
        elif menu == "2":
            print(menus[2])
            api.menu_2(arg = "https://www.melon.com/chart/index.htm")
        else : print("잘못 된 값")
