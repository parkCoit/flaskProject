
import cv2 as cv
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt


from services import ExecuteLambda, Hough, Haar
from util.dataset import Dataset


class LennaController(object):
    ds = Dataset()
    def __init__(self):
        pass

    def __str__(self):
        pass

    @staticmethod
    def menu_0(*params):
        print(params[0])
    @staticmethod
    def menu_1(*params):
        print(params[0])
        img = ExecuteLambda('IMAGE_READ_FOR_CV',params[1])
        cv.imshow("Original", img)
        cv.waitKey(0)
        cv.destroyAllWindows()

    @staticmethod
    def menu_2(*params):
        print(params[0])
        img = ExecuteLambda("URL", params[1])
        img = ExecuteLambda('GRAYSCALE', img)  # img = gray_scale(img.get())
        plt.imshow(ExecuteLambda("IMAGE_FROM_ARRAY", img))
        plt.show()


    @staticmethod
    def menu_3(*params):
        print(params[0])
        img = ExecuteLambda("URL", params[1])
        edges = cv.Canny(np.array(img), 100, 200)
        plt.subplot(121), plt.imshow(img, cmap='gray')
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(edges, cmap='gray')
        plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
        plt.show()

    @staticmethod
    def menu_4(*params):
        print(params[0])
        img = ExecuteLambda("URL", params[1])
        girl_canny = cv.Canny(img, 100, 200)

        girl_hough = Hough(girl_canny)

        plt.subplot(121), plt.imshow(img, cmap='gray')
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(girl_hough, cmap='gray')
        plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
        plt.show()


    @staticmethod
    def menu_5(*params):
        print(params[0])
        ds = Dataset()
        haar = cv.CascadeClassifier(f"{ds.context}{params[1]} ")
        girl = params[2]
        girl_original = ExecuteLambda("IMAGE_READ_FOR_CV_PLT", girl)
        girl_gray = ExecuteLambda("GRAYSCALE", girl_original)
        girl_canny = cv.Canny(np.array(girl_original), 10, 100)
        lines = cv.HoughLinesP(girl_canny, 1, np.pi / 180., 120, minLineLength=50, maxLineGap=5)
        girl_hough = cv.cvtColor(girl_canny, cv.COLOR_GRAY2BGR)
        if lines is not None:
            for i in range(lines.shape[0]):
                pt1 = (lines[i][0][0], lines[i][0][1])
                pt2 = (lines[i][0][2], lines[i][0][3])
                cv.line(girl_hough, pt1, pt2, (255, 0, 0), 2, cv.LINE_AA)



        plt.subplot(151), plt.imshow(girl_original, cmap='gray')
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])

        Haar(girl_hough, girl_original, haar, lines)

        plt.subplot(152), plt.imshow(girl_gray, cmap='gray')
        plt.title('Gray Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(153), plt.imshow(girl_canny, cmap='gray')
        plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(154), plt.imshow(girl_hough, cmap='gray')
        plt.title('Hough Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(155), plt.imshow(girl_original, cmap='gray')
        plt.title('HAAR Image'), plt.xticks([]), plt.yticks([])
        plt.show()



    @staticmethod
    def menu_6(*params):
        pass












