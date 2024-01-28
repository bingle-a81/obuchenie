from random import randint


SIZE_GAME_POLE = 10


class Ship:


    def __init__(self, length, tp=1, x=None, y=None) -> None:
        self._tp = tp
        self._length = length
        self._is_move = True
        self._cells = [1 for x in range(self._length)]
        self._orient = self._set_tp()
        self.set_start_coords(x, y)

    def _set_tp(self):
        res = (1,0)
        if self._tp == 2:
            res = (0,1)
        return res

    def get_start_coords(self):
        return (self._x, self._y)

    def set_start_coords(self, x, y):
        self._x=x
        self._y=y
        if all([x is not None,y is not None]):
            self._rect_x_nach=self._x-1
            self._rect_y_nach=self._y-1
            self._rect_x_kon=self._x+self._length*self._orient[0]+1
            self._rect_y_kon=self._y+self._length*self._orient[1]+1

    def move(self, go):
            
            x,y=self.get_start_coords()
            a = x + self._orient[0] * go
            b = y + self._orient[1] * go
            self.set_start_coords(a, b)        

    def is_collide(self, ship):
        if all([self._x is not None, self._y is not None,ship._x is not None,ship._x is not None]):
            if not (self._x+self._length*self._orient[0]<ship._rect_x_nach or 
                self._x>ship._rect_x_kon or
                self._y>ship._rect_y_kon or
                self._y+self._length*self._orient[1]<ship._rect_y_nach):
                return True
        return False
    
    def is_out_pole(self, size):
        for e in range(self._length):
            if not all(
                [
                    0 <= self._x + e * self._orient[0] < size,
                    0 <= self._y + e * self._orient[1] < size,
                ]
            ):
                return True
        return False
    
    def __getitem__(self, item):
        return self._cells[item]

    def __setitem__(self, item, val):
        self._cells[item] = val


    def __repr__(self) -> str:
        ls=[]
        for e in range(self._length):
            ls.append([self._x+e*self._orient[0],self._y+e*self._orient[1]])
        print(ls)
        return ''



class GamePole:
    def __init__(self, size) -> None:
        self._ships = [
            Ship(4, tp=randint(1, 2)),
            Ship(3, tp=randint(1, 2)),
            Ship(3, tp=randint(1, 2)),
            Ship(2, tp=randint(1, 2)),
            Ship(2, tp=randint(1, 2)),
            Ship(2, tp=randint(1, 2)),
            Ship(1, tp=randint(1, 2)),
            Ship(1, tp=randint(1, 2)),
            Ship(1, tp=randint(1, 2)),
            Ship(1, tp=randint(1, 2)),
        ]
        self._size = size
        self.pole = [[0 for i in range(self._size)] for j in range(self._size)]

    def init(self):
        for ship in self._ships:
            ship = self._add_ships(ship)
            

    def _add_ships(self, ship:Ship) -> Ship:
        i=0
        while True:
            a, b = randint(0, self._size), randint(0, self._size)
            ship.set_start_coords(a,b)
            if self.__check_ship(ship):
                return ship
            else:
                i+=1
                if i>20:
                    self.__chit()
                    break
                continue

    def __chit(self):
         self._ships = [
            Ship(4, tp=1,x=0,y=0),
            Ship(3, tp=1,x=0,y=2),
            Ship(3, tp=1,x=0,y=4),
            Ship(2, tp=1,x=0,y=6),
            Ship(2, tp=2,x=5,y=0),
            Ship(2, tp=2,x=7,y=0),
            Ship(1, tp=randint(1, 2),x=5,y=3),
            Ship(1, tp=randint(1, 2),x=5,y=5),
            Ship(1, tp=randint(1, 2),x=5,y=7),
            Ship(1, tp=randint(1, 2),x=7,y=7),
        ]       

    def __check_ship(self,ship:Ship):
            if not ship.is_out_pole(self._size ) and not any(ship.is_collide(x) for x in self._ships if ship!=x): 
                return True
            else:
                return False
                      


    def get_ships(self):
        return self._ships

    def move_ships(self):
        for ship in self._ships:
            if ship._is_move:
                ship.move(1)
                if not self.__check_ship(ship):
                    ship.move(-2)
                    if not self.__check_ship(ship):
                        ship.move(1)

    def show(self):
        temp_pole = [[0 for i in range(self._size)] for j in range(self._size)]
        for ship in self.get_ships():
            s = ship._orient
            for e in range(ship._length):
                x, y = ship.get_start_coords()
                temp_pole[x + e * s[0]][y + e * s[1]] = ship[e]
        for i in range(self._size):
            for j in range(self._size):
                print(temp_pole[i][j], end=" ")
            print("")
        print("-" * 20)

    def get_pole(self):
        temp_pole = [[0 for i in range(self._size)] for j in range(self._size)]
        for ship in self.get_ships():
            s = ship._orient
            for e in range(ship._length):
                x, y = ship.get_start_coords()
                temp_pole[x + e * s[0]][y + e * s[1]] = ship[e]
        tmp_tuple=tuple(tuple(x) for x in temp_pole)
        return tmp_tuple
        


pole = GamePole(8)
pole.init()
for x in pole._ships:
    print(x)

pole.show()

# print(pole.get_ships())

# pole.move_ships()

# print(pole.get_ships())
# pole.show()
# quit(-1)
# ------------------------------

quit(-1)
class SeaBattle:
    ...

# pole_size_8 = GamePole(9)
# pole_size_8.init()
# quit(-1)

ship = Ship(2)
ship = Ship(2, 1)
ship = Ship(3, 2, 0, 0)

assert ship._length == 3 and ship._tp == 2 and ship._x == 0 and ship._y == 0, "неверные значения атрибутов объекта класса Ship"
assert ship._cells == [1, 1, 1], "неверный список _cells"
assert ship._is_move, "неверное значение атрибута _is_move"

ship.set_start_coords(1, 2)
assert ship._x == 1 and ship._y == 2, "неверно отработал метод set_start_coords()"
assert ship.get_start_coords() == (1, 2), "неверно отработал метод get_start_coords()"

ship.move(1)
s1 = Ship(4, 1, 0, 0)
s2 = Ship(3, 2, 0, 0)
s3 = Ship(3, 2, 0, 2)

assert s1.is_collide(s2), "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 0, 0)"
assert s1.is_collide(s3) == False, "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 0, 2)"

s2 = Ship(3, 2, 1, 1)
assert s1.is_collide(s2), "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 1, 1)"

s2 = Ship(3, 1, 8, 1)
assert s2.is_out_pole(10), "неверно работает метод is_out_pole() для корабля Ship(3, 1, 8, 1)"

s2 = Ship(3, 2, 1, 5)
assert s2.is_out_pole(10) == False, "неверно работает метод is_out_pole(10) для корабля Ship(3, 2, 1, 5)"

s2[0] = 2
assert s2[0] == 2, "неверно работает обращение ship[indx]"

p = GamePole(10)
p.init()
for nn in range(5):
    for s in p._ships:
        assert s.is_out_pole(10) == False, "корабли выходят за пределы игрового поля"

        for ship in p.get_ships():
            if s != ship:
                assert s.is_collide(ship) == False, "корабли на игровом поле соприкасаются"
    p.move_ships()
    
gp = p.get_pole()
assert type(gp) == tuple and type(gp[0]) == tuple, "метод get_pole должен возвращать двумерный кортеж"
assert len(gp) == 10 and len(gp[0]) == 10, "неверные размеры игрового поля, которое вернул метод get_pole"

