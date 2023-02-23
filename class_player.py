class player:  # Main player class, responsible for holding player's attributes
    def __init__(self, life, name):
        self.maximas = { "Max_Char": 100, "Max_Life": life, "Max_Weight": 100, "Max_Exp": 9999}
        self.stats = {"Name": name, "Life": life, "Weight": 0, "Exp": 0}
        self.perks = {
                    "Attack": 5,
                    "Defense": 5,
                    "Vitality": 5,
                    "Agility": 5,
                    }
        self.status = {
                    '*Bleeding': 0,
                    '*Confusion': 0,
                    '*Shock': 0,
                    }

    def check_status(self):   # Function responsible for displaying status of a player
        for i in range(len(self.maximas)) :
            if i > 1:
                    print(list(self.maximas())[i])
                    print(str(self.stats[i]) + "/" + str(self.maximas[j]))
            else:
                print(str(list(self.stats())[i]) + ":" + str(list(self.stats.values())[i]))
        


player = player(100, 'Lucas')

player.check_status()