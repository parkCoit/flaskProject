from dataclasses import dataclass


@dataclass
class Foo:
    x = 30 # 인스턴스 변수


    def foo(self):
        x = self.x # 인스턴스 변수
        print(x)

x = 10

def foo():
    x = 20
    print(x)

def A():
    x = 10
    def B():
        x= 20
    B()
    print(x)


def C():
    x = 10
    def D():
        nonlocal x
        x = 20
    D()
    print(x)

def E():
    x = 10
    y = 100
    def F():
        x = 20
        def G():
            nonlocal x,y
            x = x+30
            y = y+300
            print("nonlocal x:"+str(x))
            print("nonlocal y:"+str(y))
        G()
    F()

def AB():
    x = 10
    def CD():
        x = 20
        def DF():
            global x
            x = x+30
            print(x)
        DF()
    CD()

def calc():
    a = 3
    b = 5
    def mul_add(x,y):
        return a*x+b + y

    def mul_add2(x,y):
        return a*x+b - y

    return {"덧셈":mul_add,"뺄셈":mul_add2}

def calc_lambda():
    a = 3
    b = 5
    return lambda x,y: a * x + b +y

def calc_nonlocal():
    a = 3
    b = 5
    t = 1
    def mul_add(x, y):
        nonlocal t
        t = t + a * x +b + y
        return t
    return mul_add



if __name__ == '__main__':
    f = Foo()
    f.foo()
    foo()
    print(x)
    A()
    C()
    E()
    AB()
    print(calc()["덧셈"](1,2), calc()["덧셈"](2,3), calc()["덧셈"](3,4))
    print(calc()["뺄셈"](1, 2), calc()["뺄셈"](2, 3), calc()["뺄셈"](3, 4))
    print(calc_lambda()(1,2), calc_lambda()(2,3), calc_lambda()(3,4))
    print(calc_nonlocal()(1,2), calc_nonlocal()(2,3), calc_nonlocal()(3,4))