
import player_fight


def name():  # Function responsible for naming a player
    print('Welcome to the game')
    print('Please choose a name for your player. Choose it wisely, as it cannot be changed later')
    while True:
        name = input()
        if isinstance(name, str):
            if name == 'changed later':
                print('I told you, it cannot be changed later')
            else:
                break
        else:
            print('Name cannot contain numbers!')
    return name


def give_points(player, inv):  # Function responsible for points distribution
    x = 10
    while x > 0:
        print('\n You have ' + str(x)+' points left \n')
        player.check_Skills(inv)
        y = input()
        if x - int(y[-1:]) + 5 < 0:
            print('Not enough points!')
            pass
        else:
            if y.lower()[:6] == 'attack':
                player.stats['Attack'] = int(y[7:])
                x -= int(y[7:]) - 5
            if y.lower()[:7] == 'defense':
                player.stats['Defense'] = int(y[8:])
                x -= int(y[8:]) - 5
            if y.lower()[:8] == 'vitality':
                player.stats['Vitality'] = int(y[9:])
                x -= int(y[9:]) - 5
            if y.lower()[:7] == 'agility':
                player.stats['Agility'] = int(y[8:])
                x -= int(y[8:]) - 5
    player.check_Skills(inv)


x = name()
print('Great. So your name is ' + x)
player = player_fight.player(100, x)  # Initialization of player and inventory
inv = player_fight.inventory_c()
# give_points(player, inv)  # points distribution
player.change_life(True)
player.change_crits()

while True:  # Main menu of a game
    x = input()
    if x.lower() == 'menu':
        player_fight.menu(inv, player)
    if x.lower() == 'go':
        player_fight.fight(inv, player)
