from bicycle.model import BicycleModel
from util.dataset import Dataset


class BicycleController(object):

    model = BicycleModel()
    dataset = Dataset()
    def __init__(self):
        pass

    def __str__(self):
        pass

    def preprocess(self, train):
        model = self.model
        this = self.dataset
        this.train = model.new_model(train)