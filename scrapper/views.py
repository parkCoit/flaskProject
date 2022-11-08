
from scrapper.services import BugsMusic, MelonMusic


class ScrapController(object):
    def __init__(self):
        pass

    def __str__(self):
        pass

    @staticmethod
    def menu_1(arg):
        BugsMusic(arg)

    @staticmethod
    def menu_2(arg):
        MelonMusic(arg)