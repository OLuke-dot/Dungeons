# In this file player and inventory class are being declared. Here is a function responsible for fight menu, as well as functions responsible for attack itself and inventory

import monsters_inc
import inventory
import random
import randomize
import pickle
from os import path
from os import listdir


class player:  # Main player class, responsible for holding player's attributes
    def __init__(self, life, name):
        self.max_life = life
        self.life = self.max_life
        self.exp = 0
        self.name = name
        self.stats = {
                    "Attack": 5,
                    "Defense": 5,
                    "Vitality": 5,
                    "Agility": 5
                    }
        self.status = {
                    '*Max_Weight': 100,
                    '*Bleeding': 0,
                    '*Confusion': 0,
                    '*Shock': 0,
                    }
        self.crit = 10
        self.low = 50
        self.vel = 15

    def check_Status(self):   # Function responsible for displaying status of a player
        print('Here are your current statuses: \n')
        print('*Life: ' + str(self.life) + '/' + str(self.max_life))
        print('*Experience: ' + str(self.exp))
        for i in self.status:
            if self.status[i] != 0:
                print(i + ': ' + str(self.status[i]))

    def check_Skills(self, var):   # Function responsible for displaying skills of a player
        print('Here are your curent skills: \n')
        for i in self.stats:
            x = 0
            for j in var.size:
                for k in j:
                    if i == k and j['Eq'] is True:
                        x += j[k]
            if x >= 0:
                print(i + ': ' + str(self.stats[i]) + "(+" + str(x) + ')')
            else:
                print(i + ': ' + str(self.stats[i]) + "(-" + str(x*-1) + ')')
            print('[', end='')
            for x in range(self.stats[i]):
                print('*', end=''),
            x = 10 - self.stats[i]
            for y in range(x):
                print('-', end=''),
            print(']\n')

    def change_life(self, var):  # Function responsible for setting up life
        self.max_life = 20 * self.stats['Vitality']
        if var is True or self.max_life < self.life:
            self.life = self.max_life
        else:
            pass

    def change_vitality(self, var):
        self.stats['Vitality'] += var

    def change_crits(self):
        x = self.stats['Agility'] - 5
        self.crit += 5 * x
        if self.low < 5*x:
            pass
        else:
            self.low -= 5 * x

    def change_agility(self, var):
        self.stats['Agility'] += var


class inventory_c():  # Main inventory class responsible for players inventory

    size = []

    def __init__(self):  # initialization
        self.size.append(inventory.items[7])
        self.size.append(inventory.items[0])
        self.size.append(inventory.items[8])
        for i in self.size:
            i['Eq'] = True

    # Function responsible for displaying inventory
    def check_inventory(self, player):
        temp_weight = 0
        for i in self.size:
            for j in i:
                if j == 'Weight':
                    temp_weight += i[j]
        print('Your weight: ' + str(temp_weight) + '/' + str(player.status['*Max_Weight']))
        for i in self.size:
            if i['Eq'] is True:
                print(i['Title'] + '(Equipped)')
            else:
                pass
        for i in self.size:
            if i['Eq'] is False:
                print(i['Title'])
            else:
                pass

    # Function responsible for item description
    def description(self, variable):
        for i in self.size:
            if i['Title'].lower() == variable.lower():
                for j in i:
                    if j == 'Eq':
                        pass
                    else:
                        print(j + ': ' + str(i[j]))

    # Function responsible for equiping items
    def equip(self, player, item_name):
        for j in inventory.items:
            if j['Title'].lower() == item_name.lower():
                item = j
                break
            else:
                pass
        for i in self.size:
            if i['Class'] == item['Class'] and i['Eq'] is True:
                self.dequip(player, i['Title'])
        # self.size.append(item)
        item['Eq'] = True
        print('You equipped ' + item['Title'] + '\n')
        for i in item:
            if str(i) == 'Vitality':
                player.change_vitality(item['Vitality'])
                player.change_life(False)
            if str(i) == 'Agility':
                player.change_agility(item['Agility'])
                player.change_crits()
            else:
                pass

    # Function responsible for dequiping items
    def dequip(self, player, item_name):
        for j in inventory.items:
            if j['Title'].lower() == item_name.lower():
                item = j
                break
            else:
                pass
        for i in self.size:
            if i['Title'].lower() == item_name.lower():
                i['Eq'] = False
            else:
                pass
        print('You hide your ' + item['Title'] + ' in your backpack\n')

    def add_to_inv(self, item_name):
        for j in inventory.items:
            if j['Title'].lower() == item_name.lower():
                item = j
                break
            else:
                pass
        print(item['Title'] + ' has been added to your inventory \n')
        self.size.append(item)

    def drop_inventory(self, item_name):
        for j in inventory.items:
            if j['Title'].lower() == item_name.lower():
                item = j
                break
            else:
                pass
        print('You removed ' + item['Title'] + ' from your inventory \n')
        self.size.pop()


def menu(inv, player):  # Function responsible for displaying and managing players menu
    print('You have opened your menu \n')
    print('-Check inventory')
    print('-Check your status')
    print('-Check your skills')
    print('-Save game')
    print('-quit')
    while True:
        x = input()
        if isinstance(x, str):
            if x.lower() == 'check inventory':
                check_inv(player, inv)
            if x.lower() == 'check status':
                player.check_Status()
            if x.lower() == 'check skills':
                player.check_Skills(inv)
            if x.lower() == 'save' or x.lower() == 'save game':
                sv_game(player, inv)
            if x.lower() == 'quit':
                print('You closed your menu')
                break
        else:
            print('Incorrect command. Type help for guidance \n')


def sv_game(player, inv):
    while True:
        print('Name your save file:')
        x = input()
        x += '.sav'
        temp = path.abspath(path.curdir)
        temp += '/Saves/'
        allow = False
        for i in listdir(temp):
            if i == x:
                print('There exists already file named ' + x +'. Would you like to overwrite it? \n')
                y = input()
                if y.lower() == 'yes' or y.lower() == 'y':
                    allow = True
                elif y.lower() == 'no' or y.lower() == 'n':
                    print('Saving aborted \n')
                    break
                else:
                    print('Unrecognized command \n Returning to menu...')
            else:
                allow = True
        try:
            if allow is True:
                with open(temp+str(x), 'bw') as f:
                    pickle.dump(player, f)
                    pickle.dump(inv, f)
                    print('Game saved.')
                    break
        except:
            print('Saving failed. Please try again')
            break


def check_inv(player, inv):  # Function responsible for displaying and managing inventory menu
    while True:
        inv.check_inventory(player)
        x = input()
        if isinstance(x, str):
            if x.lower()[:5] == 'equip':
                print('\n')
                inv.equip(player, x[6:])
            if x.lower()[:6] == 'dequip':
                print('\n')
                inv.dequip(player, x[7:])
            if x.lower()[:11] == 'description':
                inv.description(x[12:])
            if x.lower() == 'back':
                print('You went back to the menu \n')
                break
        else:
            print('Incorrect command. Type help for guidance')


def fight(inv, player):  # Function responsible for fight menu and attacker
    battle = False
    attacker = monsters_inc.minion()  # TODO change for random generation
    print('A ' + attacker.name + ' appeared in front of you! \n')
    while battle is False:
        x = input()
        if x.lower() == 'attack':
            pagil = 0
            for i in inv.size:
                for j in i:
                    if j == 'Agility' and i['Eq'] is True:
                        pagil += i[j]
                    else:
                        pass
            pagil += player.stats['Agility']
            if attacker.stats['Agility'] > pagil:
                p1 = attacker
                p2 = player
            else:
                p1 = player
                p2 = attacker
            attack(p1, p2, inv, player)
        if x.lower() == 'inspect':
            print(attacker.name)
            print('Life: ' + str(attacker.life) + '/'+str(attacker.max_life))
            for i in attacker.stats:
                print(i + ': ' + str(attacker.stats[i]))
        if x.lower() == 'check status':
            player.check_Status()
        if x.lower() == 'use inventory':
            check_inv(player, inv)
        if x.lower() == 'help':
            fight_menu()
        else:
            pass

        if attacker.life <= 0:
            print(attacker.name + ' dies! \n')
            give_exp(attacker, player)
            battle = not False
        if player.life <= 0:
            print('You have fainted... \n ')
            battle = not False


def fight_menu():
    print('-Attack')
    print('-Inspect')
    print('-Check status')
    print('-Use inventory')
    print('-Escape')


def attack(p1, p2, inv, player):  # Function responsible for displaying and managing attack sectionn
    x = p1.stats['Attack']
    y = p2.stats['Attack']
    for i in inv.size:
        for j in i:
            if j == 'Attack' and i['Eq'] is True:
                if p1.name == player.name:
                    x += i[j]
                    cv1 = p1.crit + i['Crit']
                    lv1 = p1.low + i['Low']
                    cv2 = p2.crit
                    lv2 = p2.low
                else:
                    y += i[j]
                    cv1 = p2.crit + i['Crit']
                    lv1 = p2.low + i['Low']
                    cv2 = p1.crit
                    lv2 = p1.low
            else:
                pass
    value = rando(cv1, lv1, x)
    print(p1.name + ' attacked '+p2.name+' for ' + str(value) + ' points! \n')
    p2.life -= value
    if p2.life <= 0:
        pass
    else:
        value = rando(cv2, lv2, y)
        print(p2.name + ' attacked '+p1.name+' for '+str(value)+' points \n')
        p1.life -= value


def rando(crit, low, attack):

    x = randomize.chances_generator(crit, low)
    if x == 'c':
        value = attack * ((random.randint(3, 10) + 100)/100)
        print('Critical hit! \n')
    if x == 'l':
        value = attack * (random.randint(90, 98)/100)
    if x == 'n':
        value = attack
    return int(value)


def give_exp(var, player):  # Function responsible for experience dropping
    print(var.name + ' gave you ' + str(var.exp) + ' experience')
    player.exp += var.exp
