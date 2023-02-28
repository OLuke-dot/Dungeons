import pandas as pd
import re

#TODO: add support for double-handed weapons. Add comments

class player:  # Main player class, responsible for holding player's attributes and equipment
    def __init__(self, life, name):
        self.name = name
        self.inventory = pd.DataFrame() #Players Inventory
        self.gear = pd.DataFrame() #Players current equipped gear
        self.maximas = {"Max_Life": life, "Max_Weight": 100, "Max_Exp": 9999} #Maximum life, maximal weight and experience for the player
        self.stats = {"Life": life, "Weight": 0, "Exp": 0}
        self.perks = {
                    "Attack": 5,
                    "Defense": 5,
                    "Vitality": 5,
                    "Agility": 5,
                    } #Player current stats
        self.status = {
                    '*Bleeding': 0,
                    '*Confusion': 0,
                    '*Shock': 0,
                    } #Additional statuses that can affect player
    
    # Function responsible for displaying status of a player
    def check_status(self):   
       print("Name: " + self.name)
       keys = list(self.stats.keys())
       values = list(self.stats.values())
       values_max = list(self.maximas.values())
       for i in range(0, len(self.stats)):
           print(str(keys[i]) + ":" + str(values[i]) + "/" + str(values_max[i]))
    
    #Function responsible for adding item to the inventory
    def addItem(self, param):
        if self.inventory.empty:
            self.inventory = param
        else:
            self.inventory = pd.concat([self.inventory, param])

        #self.inventory.reset_index()
        #self.inventory.index = range(1, len(self.inventory) + 1)
        self.sortIndex(self.inventory)
        print("You have added " + param.values[0, 0] + " to your inventory.")

    #Function responsible for listing full inventory
    def listInventory(self):
        titles = ['Name', 'Type', 'attack', 'defence', 'speed', 'two-hand']
        print("Equipped:")
        print(self.gear[titles])
        print("------------")
        print(self.inventory[titles])

    #Function for using equipment
    def addEquipment(self, param):
        search = param.values[0, 1]
        temp = param.values[0, 0]
        if self.gear.empty:
            self.gear = pd.concat([self.gear, param])
            print("you have equipped " + param.values[0, 0])
            self.inventory = self.inventory.drop(self.inventory[self.inventory.values[0,0] == param.values[0, 0]]) #<--- to fix, not working now
        else:
           for i in range(len(self.gear)):
                if search == self.gear.values[i, 1]:
                    x = input('Do you want to change ' + self.gear.values[i, 0] + " for " + param.values[i, 0] + "? \n")
                    if re.findall("Y..?", x):
                        self.inventory = pd.concat([self.inventory, self.gear.iloc[[i]]]) #Adding previous item to inventory
                        value = self.gear.index[self.gear['Type']==search].tolist()
                        self.gear = self.gear.drop(value) #Removing previous item from gear
                        self.gear = pd.concat([self.gear, param]) #Adding new item to the gear
                        print("You have equipped " + param.values[0, 0])
                    else:
                        pass
                else:
                    self.gear = pd.concat([self.gear, param])
                    print("you have equipped " + param.values[0, 0])
                    self.inventory = self.inventory.drop(index=param.index) 
        self.sortIndex(self.inventory)
        self.sortIndex(self.gear)

    def sortIndex(self, dataFrame):
        dataFrame.reset_index()
        dataFrame.index = range(1, len(dataFrame) + 1)
        return dataFrame




player = player(100, 'Lucas')

items = pd.read_csv('items.csv')
items['two-hand'] = items['two-hand'].map({0: 'No', 1: 'Yes'})

player.addItem(items.sample())
temp = items.sample()
player.addItem(temp)
player.addEquipment(temp)
player.listInventory()
player.check_status()