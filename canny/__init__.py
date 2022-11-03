

from canny.views import LennaController
from util.common import Common



Lenna = "Lenna.png"
Soccer = "https://docs.opencv.org/4.x/roi.jpg"
Line = "http://amroamroamro.github.io/mexopencv/opencv_contrib/fast_hough_transform_demo_01.png"
HAAR = "haarcascade_frontalface_alt.xml"
GIRL = "girl.jpg"
GIRL_INCLIEND = "girl_incliend.png"
GIRL_SIDE_FACE = "girl_side_face.jpg"
GRIL_WITH_MOM = "girl_with_mom.jpg"
CAT = "cat.jpg"
FACE_TARGET = ""
FACE_OBJECT = ""
if __name__ == '__main__':

    api = LennaController()

    while True:
        menus =["종료", "원본보기", "그레이스케일", "엣지검출"
                ,"직선검출", "얼굴인식", "모자이크","얼굴추출"]
        menu = Common.menu(menus)
        if menu == "0":
            api.menu_0(menus[0])
            break
        elif menu == "1" :
            api.menu_1(menus[1], Lenna)

        elif menu == "2" :
            api.menu_2(menus[2], Soccer)

        elif menu == "3" :
            api.menu_3(menus[3], Soccer)

        elif menu == "4" :
            api.menu_4(menus[4], Line)

        elif menu == "5" :
            api.menu_5(menus[5],HAAR, GIRL)

        elif menu == "6" :
            api.menu_6(menus[6], CAT)

        else : print("### 잘못 된 값 ###")
