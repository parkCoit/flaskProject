from randomlist import Randomlist

class OddEven(object):
    def __init__(self) -> None:
        pass

    @staticmethod
    def print():
        rl = Randomlist().get_random(1,100,10)
        print(rl)
        for i in rl:
            if i % 2 == 0 :
                print(f"짝수 : {i}" )
            else:
                print(f"홀수 : {i}")

        print([ f"짝수 : {i}" if i % 2 == 0 else f"홀수 : {i}" for i in rl])



    @staticmethod
    def main():
        oddeven = OddEven()
        oddeven.print()

OddEven.main()