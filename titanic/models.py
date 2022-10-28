import pandas as pd


from util.dataset import Dataset

"""
 ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
 시각화를 통해 얻은 상관관계 변수(variable = feature = column)는
 === 상관 관계 ===
 Pclass 
 Sex
 Age
 Fare
 Embarked
 === null 값 === null 값 있을땐 for 문 돌리면 에러걸림
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
    @staticmethod
    def pclass_ordinal(this) -> object: # 1, 2, 3등칸
        train = this.train
        test = this.test
        return this
    @staticmethod
    def sex_norminal(this) -> object: # female -> 1 , male -> 0
        for i in [this.train, this.test]:
            i['Gender'] = i['Sex'].map({"male" : 0, "female" : 1}) # mapping 할때 쓰는게 dc임
        return this
    @staticmethod
    def age_ordinal(this) -> object: # 10대, 20대, 30대
        train = this.train
        test = this.test
        return this
    @staticmethod
    def fare_ordinal(this) -> object: # 비싼거, 보통, 저렴한 것  4등분 pd.qcut()
        for i in [this.train, this.test]:
            i['FareBand'] = pd.qcut(i['Fare'], 4, labels=[1, 2, 3, 4] )
        return this
    @staticmethod
    def embarked_nominal(this) -> object: # 승선항구 S, C, Q
        this.train = this.train.fillna({"Embarked":"S"})    # fillna 는 null 값을 임의로 넣으라는 뜻
        this.test = this.test.fillna({"Embarked": "S"})
        for i in [this.train, this.test]:
            i['Embarked'] = i['Embarked'].map({"S": 1, "C" : 2, "Q" : 3}) # 같은 이름을 넣으면 원래 이름에 덮어짐 train,test에 스칼라가 추가 되는 것이 아님.
        return this

if __name__ == '__main__':
    t = TitanicModel()
    this = Dataset()
    this.train = t.new_model('train.csv')
    this.test = t.new_model('test.csv')
    this = TitanicModel.sex_norminal(this)
    this = TitanicModel.fare_ordinal(this)
    this = TitanicModel.embarked_nominal(this)
    print(this.train.columns)
    print(this.train.head())
    print(this.test.columns)