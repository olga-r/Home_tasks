from collections import defaultdict
from random import choice, randint
from string import ascii_uppercase
from itertools import product

class Field(object):
    def __init__(self):
        self.height = 10
        self.width = 10
        self.ships = defaultdict(list)
        self.occupied_cells = set()
    def create_ships(self):
        for i, sh in enumerate(range(4, 0, -1)):
            for s in range(1, i+2):
                self.ships['ship{}_{}'.format(sh, s)] = Ship(sh)
    def check_cells(self, ship):
        for cell in ship.pos:
            if cell in self.occupied_cells:
                return None
        for cell in ship.area:
            self.occupied_cells.add(cell)
        return ship.pos
    def result_of_attack(self, X, Y):
        pass
            
class Ship(object):
    def __init__(self, size):
        self.size = size
        self.pos = []
        self.area = []
    
    def rnd_pos(self, f):
        while True:
            self.x1 = randint(1, f.width)
            self.x = ascii_uppercase[self.x1-1]
            self.y = randint(1, f.height)
            ax =  (self.x1-1) if self.x1 > 1 else 1
            bx = (self.x1+2) if self.x1 < 10 else 11
            a1x = (self.x1+1) if self.x1 < 10 else 10
            b1x = (self.x1-self.size-1) if (self.x1-self.size) > 0 else 0
            b2x = (self.x1+self.size+1) if (self.x1+self.size) < 11 else 11
            ay =  (self.y-1) if self.y > 1 else 1
            by = (self.y+2) if self.y < 10 else 11
            a1y = (self.y+1) if self.y < 10 else 10
            b1y = (self.y-self.size-1) if (self.y-self.size) > 0 else 0
            b2y = (self.y+self.size+1) if (self.y+self.size) < 11 else 11
            if (self.x, self.y) not in f.occupied_cells:
                self.direct = choice('NWES')
                if self.direct == 'N' and (self.y-self.size) >= 0:
                    # Кирилл, скажите, пожалуйста, почему, когда я не делала list из product, у меня итерация в методе field.check_cells не шла
                    self.pos = list(product(self.x, range(self.y, self.y-self.size,-1)))
                    self.area = list(product([ascii_uppercase[i-1] for i in range(ax, bx)], range(a1y, b1y,-1)))
                elif self.direct == 'S' and (self.y+self.size) <= 11 :
                    self.pos = list(product(self.x, range(self.y, self.y+self.size)))
                    self.area = list(product([ascii_uppercase[i-1] for i in range(ax, bx)], range(ay, b2y)))
                elif self.direct == 'E' and (self.x1+self.size) <= 11:
                    self.pos = list(product([ascii_uppercase[i-1] for i in range(self.x1, self.x1+self.size)], [self.y]))
                    self.area = list(product([ascii_uppercase[i-1] for i in range(ax, b2x)], range(ay, by)))
                elif self.direct == 'W' and (self.x1-self.size) >= 0:
                    self.pos = list(product([ascii_uppercase[i-1] for i in range(self.x1, self.x1-self.size, -1)], [self.y]))
                    self.area = list(product([ascii_uppercase[i-1] for i in range(a1x, b1x, -1)], range(ay, by)))
                if f.check_cells(self):
                    break
        return self.pos   
                              
     
field = Field()
field.create_ships()
for k, v in field.ships.items():
    v.rnd_pos(field)
    print(k, v.size, v.pos)
    