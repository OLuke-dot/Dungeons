import random


class monster:

    def __init__(self):
        pass


class minion(monster):
    def __init__(self):
        self.name = 'Minion monster'
        self.stats = {
                    "Attack": 10,
                    "Defense": 10,
                    "Vitality": 10,
                    "Agility": 8
                    }
        self.life = 25
        self.max_life = self.life
        self.exp = 25
        self.crit = 10
        self.low = 50
