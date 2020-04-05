import random


class map_generator():

    def __init__(self, x, y):
        self.map = []
        for j in range(11):
            self.column = []
            for i in range(11):
                self.column.append(' ')
            self.map.append(self.column)
        self.map[x][y] = 'o'
        if x-1 == 0 or y-1 == 0:
            pass
        else:
            self.map[x-1][y-1] = 'x'
        if x+1 > 11 or y-1 < 0:
            pass
        else:
            self.map[x+1][y-1] = 'x'
        if x-1 < 0 or y+1 > 11:
            pass
        else:
            self.map[x-1][y+1] = 'x'
        if x+1 > 11 or y+1 > 11:
            pass
        else:
            self.map[x+1][y+1] = 'x'

    def print_map(self):
        for i in range(11):
            print('| ',  end=''),
            for j in range(11):
                print(self.map[i][j]+' | ',  end=''),
            print('\n')
        for i in range(12):
            print('- ', end=''),
        print('\n')

    def generator(self):
        for i in range(11):
            for j in range(11):
                x = random.choice([True, False])
                if x is True:
                    if self.map[i][j] == 'x' or self.map[i][j] == 'o':
                        pass
                    else:
                        self.map[i][j] = 'x'
                else:
                    pass


x = map_generator(0, 0)
# x.generator()
x.print_map()
