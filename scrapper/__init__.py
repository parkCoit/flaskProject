from scrapper.domains import Scrap
from scrapper.views import ScrapController
from util.common import Common



if __name__ == '__main__':
    api = ScrapController()
    scrap = Scrap()
    while True :
        menus = ["종료", "벅스뮤직", "멜론뮤직"]
        menu = Common.menu(menus)
        if menu == "0":
            print(menus[0])
            break
        elif menu == "1":
            print(menus[1])
            scrap.domain = "https://music.bugs.co.kr/chart/track/day/total?chartdate="
            scrap.query_string = "20221101"
            scrap.parser = "lxml"
            scrap.class_names= ["title","artist"]
            scrap.tag_name = "p"
            api.menu_1(scrap)
        elif menu == "2":
            print(menus[2])
            scrap.headers = {'User-Agent' : "Mozilla/5.0"}
            scrap.domain = "https://www.melon.com/chart/index.htm"
            scrap.parser = "lxml"
            scrap.class_names = ["rank01", "rank03"]
            scrap.tag_name ="div"
            api.menu_2(scrap)
        else : print("잘못 된 값")
