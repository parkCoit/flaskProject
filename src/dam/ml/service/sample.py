
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier


def execute():
    clf = RandomForestClassifier(random_state=0)
    X = [[1,2,3], [11,12,13]] # 확률변수 : 샘플 2개, 피쳐 3개
    y = [0,1] # 기대갑, 예측값 E : 각 샘플의 클래스(타깃변수의 클래스값)
    clf2 = DecisionTreeClassifier(random_state=0)
    print(clf2.fit(X,y))
    print(clf.fit(X,y)) # clf 객체를 통해 학습시킨다.
    print(clf.predict([[6,7,8], [14,15,16]]))
    print(clf2.predict([[6,7,8], [14,15,16]]))
    # 새로운 데이터셋의 클래스를 예측
if __name__ == '__main__':
    execute()