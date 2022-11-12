from io import BytesIO

import numpy as np
from PIL import Image
from sphinx.util import requests
import cv2 as cv
from util.dataset import Dataset


def MosaicLambda(*params):
    ds = Dataset()
    cmd = params[0]
    target = params[1]
    ds.context = "./data/"
    if cmd == "IMAGE_READ_FOR_CV":
        return (lambda x: cv.imread(f'{ds.context}{x}'))(target)
    elif cmd == "IMAGE_READ_FOR_CV_PLT":
        return cv.cvtColor((lambda x: cv.imread(f'{ds.context}{x}'))(target), cv.COLOR_BGR2RGB)
    elif cmd == "GRAYSCALE":
        return (lambda x: x[:, :, 0] * 0.114 + x[:, :, 1] * 0.587 + x[:, :, 2] * 0.229)(target)
    elif cmd == "IMAGE_FROM_ARRAY":
        return (lambda x: Image.fromarray(x) )(target)
    elif cmd == "URL":
        return (lambda x: np.array(Image.open(BytesIO(requests.get(x, headers={'User-Agent': 'My User Agent 1.0'}).content))))(target)


