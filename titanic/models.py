import pandas as pd

from util.dataset import Dataset
"""
 ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
 === null 값 ===
 Age      177
 Cabin     687
 Embarked  2
 """


class TitanicModel(object):

    dataset = Dataset()
    def __init__(self):
        pass

    def __str__(self):
        b = self.new_model(self.dataset.fname)
        return f" Train type : {type(b)} \n" \
               f"Train columns : {b.columns} \n" \
               f"Train head : {b.head()}\n" \
               f"Train null의 갯수 : {b.isnull().sum()}"

    def preprocess(self):
        pass

    def new_model(self, fname):
        this = self.dataset
        this.context = './data/'
        this.fname = fname
        return pd.read_csv(this.context + this.fname)
    @staticmethod
    def create_train(this) -> object:
        return this.train.drop('Survived', axis = 1) # drop은 dataset 에 있는 train에있는 Suvived열을 지운다
    @staticmethod
    def create_label(this) -> object: # test용은 label
        return this.train['Survived']

    @staticmethod
    def drop_features(this, *feature) -> object: # *feature 에잇는 *은 지료구조라는 표시임
        for i in feature:
            this.train = this.train.drop(i, axis = 1)
            this.test = this.test.drop(i, axis = 1)
        return this