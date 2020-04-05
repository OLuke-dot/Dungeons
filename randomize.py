# This is a file in which random numbers ae generated
import random


def chances_generator(crit, low):
    table = []
    for i in range(0, crit):
        table.append('c')
    for i in range(0, low):
        table.append('l')
    temp = (100 - (crit+low))
    for i in range(0, temp):
        table.append('n')
    random_number = random.choice(table)
    return random_number
