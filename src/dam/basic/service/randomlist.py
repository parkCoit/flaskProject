import random

class Randomlist(object):

    def __init__(self) -> None:
        pass

    def get_random(self, start, end, count):  # get return 존재 set return x
        return random.sample(range(start,end), k=count) # range 는 내장되있다

    def print(self):
        print(self.get_random(10, 100, 10))

"""   wrapping 제거 
    @staticmethod
    def main():
        rl = Randomlist()
        rl.print()
"""

if __name__=="__main__":
    rl = Randomlist()
    rl.print()