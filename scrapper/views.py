from scrapper import MusicRanking
from scrapper.services import BugsMusic, MelonMusic


class ScrapperController(object):
    def __init__(self):
        pass

    def __str__(self):
        pass

    @staticmethod
    def menu_1(arg):
        arg = MusicRanking()
        BugsMusic(arg)

    @staticmethod
    def menu_2(arg):
        melon = MelonMusic()
        melon.scraps()