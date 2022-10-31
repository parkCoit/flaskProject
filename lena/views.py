

from lena.models import LennaModel
from util.dataset import Dataset


class LennaController(object):
    def __init__(self):
        pass

    def __str__(self):
        pass

    dataset = Dataset()
    model = LennaModel()

    def preprocess(self, fname):
        model = self.model
        img = model.new_model(fname)
        return img



    def modelling(self, fname):
        img = self.preprocess(fname)
        return img


