import copy

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


from services import Hough, Haar, Mosaic, Mosaics
from util.dataset import Dataset
from util.lambdas import MosaicLambda

ds = Dataset()
ds.context = "./data/"


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
        img = MosaicLambda('IMAGE_READ_FOR_CV',params[1])
        cv.imshow("Original", img)
        cv.waitKey(0)
        cv.destroyAllWindows()

    @staticmethod
    def menu_2(*params):
        print(params[0])
        img = MosaicLambda("URL", params[1])
        img = MosaicLambda('GRAYSCALE', img)  # img = gray_scale(img.get())
        plt.imshow(MosaicLambda("IMAGE_FROM_ARRAY", img))
        plt.show()


    @staticmethod
    def menu_3(*params):
        print(params[0])
        img = MosaicLambda("URL", params[1])
        edges = cv.Canny(np.array(img), 100, 200)
        plt.subplot(121), plt.imshow(img, cmap='gray')
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(edges, cmap='gray')
        plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
        plt.show()

    @staticmethod
    def menu_4(*params):
        print(params[0])
        img = MosaicLambda("URL", params[1])
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
        cat = MosaicLambda("IMAGE_READ_FOR_CV_PLT", params[1])
        mos = Mosaic(cat ,(150,150,200,200),  10)
        cv.imwrite(f'{Dataset().context}cat-mosaic.png', mos)
        cv.imshow("CAT MOSAIC", mos)
        cv.waitKey(0)
        cv.destroyAllWindows()

    @staticmethod
    def menu_6(*params):
        print(params[0])
        haar = cv.CascadeClassifier(f"{ds.context}{params[2]} ")
        girl = params[1]

        girl_original = MosaicLambda("IMAGE_READ_FOR_CV_PLT", girl)
        girl_clone = copy.deepcopy(girl_original)
        girl_gray = MosaicLambda("GRAYSCALE", girl_original)
        girl_canny = cv.Canny(np.array(girl_original), 10, 100)
        girl_hough = Hough(girl_canny)

        Haar(girl_clone, haar)
        dst = Mosaics(girl_original, haar, 10)

        plt.subplot(231), plt.imshow(girl_original, cmap='gray')
        plt.title('Original'), plt.xticks([]), plt.yticks([])
        plt.subplot(232), plt.imshow(girl_gray, cmap='gray')
        plt.title('Gray'), plt.xticks([]), plt.yticks([])
        plt.subplot(233), plt.imshow(girl_canny, cmap='gray')
        plt.title('Edge'), plt.xticks([]), plt.yticks([])
        plt.subplot(234), plt.imshow(girl_hough, cmap='gray')
        plt.title('Hough'), plt.xticks([]), plt.yticks([])
        plt.subplot(235), plt.imshow(girl_clone, cmap='gray')
        plt.title('HAAR'), plt.xticks([]), plt.yticks([])
        plt.subplot(236), plt.imshow(dst, cmap='gray')
        plt.title('Mosaic'), plt.xticks([]), plt.yticks([])
        plt.show()
    @staticmethod
    def menu_7(*params):
        print(params[0])
        ds.context = "./data/"
        Girl_with_mom = MosaicLambda("IMAGE_READ_FOR_CV_PLT", params[1])
        haar = cv.CascadeClassifier(f"{ds.context}{params[2]} ")
        girl_with_mom = Mosaics(Girl_with_mom, haar, 10)

        plt.subplot(111), plt.imshow(girl_with_mom, cmap='gray')
        plt.title('Mosaic'), plt.xticks([]), plt.yticks([])
        plt.show()






















