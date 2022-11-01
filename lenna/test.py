from io import BytesIO

import cv2
import numpy as np
import requests
from PIL import Image
from matplotlib import pyplot as plt


class Test(object):
    def __init__(self):
        headers = {'User-Agent': 'My User Agent 1.0'}
        res = requests.get('https://slack-imgs.com/?c=1&o1=ro&url=https%3A%2F%2Fdocs.opencv.org%2F4.x%2Froi.jpg', headers)
        self.img = np.array(Image.open(BytesIO(res.content)))
        self.edges = cv2.Canny(self.img, 100, 200)


    def gray_scale(self):
        plt.subplot(121), plt.imshow(self.img, cmap='gray')
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        plt.show()

    def canny(self):
        plt.subplot(122), plt.imshow(self.edges, cmap='gray')
        plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
        plt.show()

if __name__ == '__main__':
    Test().gray_scale()
    Test().canny()