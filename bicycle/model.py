import pandas as pd

from util.dataset import Dataset


class BicycleModel(object):

    dataset = Dataset()
    def __init__(self):
        pass

    def __str__(self):
        b = self.new_model('train.csv')
        return f' Train type :{type(b)}' \
               f'Train columns :{b.columns}'
        """
        print(f' Train type :{type(b)}')
        print(f' Train columns :{b.columns}')
        print(f' Train head : {b.head()}')
        print(f' Train null 의 갯수 : {b.isnull().sum()}')"""

    def preprocess(self):
        pass

    def new_model(self, fname):
        this = self.dataset
        this.context = './data/'
        this.fname = fname
        return pd.read_csv(this.context + this.fname)

    def create_train(self):
        pass

