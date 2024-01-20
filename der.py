from random import randint


SIZE_GAME_POLE = 10


class Ship:
    ship_lst = []

    def __init__(self, length, tp=1, x=None, y=None) -> None:
        self._tp = tp
        self._length = length
        self._is_move = True
        self._cells = [1 for x in range(self._length)]
        self._orient = self._set_tp()
        if (x is not None) and (y is not None):
            self.set_start_coords(x, y)

    def _set_tp(self):
        res = (1, 0)
        if self._tp == 2:
            res = (0, 1)
        return res

    def set_start_coords(self, x, y):
        self._x = x
        self._y = y
        if self not in self.ship_lst:
            self.ship_lst.append(self)

    def get_start_coords(self):
        return (self._x, self._y)

    def move(self, go):
        if self._is_move == True:
            x1, y1 = self._x, self._y
            i=0
            while i<2:
                a = self._x + self._orient[0] * go
                b = self._y + self._orient[1] * go
                self.set_start_coords(a, b)
                if self.is_out_pole(SIZE_GAME_POLE) == False:
                    
                    if self.is_collide(self) == False:
                        self.set_start_coords(a, b)
                        return
                i+=1
                go=go*(-1)
            self.set_start_coords(x1, y1)

    def is_collide(self, ship):
        a,b=ship._x,ship._y
        ship.set_start_coords(-10, -10)
        lst = Ship._set_pole()
        for e in range(self._length):
            if lst[a + e * self._orient[0]][b + e * self._orient[1]] != 0:
                ship.set_start_coords(a,b)
                return True
        ship.set_start_coords(a,b)
        return False

        # if all(
        #     lst[self._x + e * self._orient[0]][self._y + e * self._orient[1]] == 0
        #     for e in range(self._length)
        # ):

        # else:
        #     return True

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
        return f"{self._length}:({self._x},{self._y}),{self._tp}"

    @classmethod
    def _set_pole(cls) -> list:
        pole = [[0 for i in range(SIZE_GAME_POLE)] for j in range(SIZE_GAME_POLE)]
        c = (
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 0),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        )
        for ship in cls.ship_lst:

            for e in range(ship._length):
                for i in c:
                    if (
                        0 <= ship._x + e * ship._orient[0] + i[0] < SIZE_GAME_POLE
                    ) and (0 <= ship._y + e * ship._orient[1] + i[1] < SIZE_GAME_POLE):
                        pole[ship._x + e * ship._orient[0] + i[0]][
                            ship._y + e * ship._orient[1] + i[1]
                        ] = 5
        return pole


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
            x, y = self._add_ships(ship)
            ship.set_start_coords(x, y)

    def _check_point(self, x, y):
        if (
            all([0 <= x < self._size, 0 <= y < self._size])
            and Ship._set_pole()[x][y] == 0
        ):
            return True
        return False

    def _add_ships(self, ship) -> tuple:
        s = (1, 0)
        if ship._tp == 2:
            s = (0, 1)
        while True:
            a, b = randint(0, self._size), randint(0, self._size)
            if all(
                [
                    self._check_point(a + e * s[0], b + e * s[1])
                    for e in range(ship._length)
                ]
            ):
                return a, b

    def get_ships(self):
        return self._ships

    def move_ships(self):
        for ship in self._ships:
            ship.move(1)

    def show(self):
        temp_pole = [[0 for i in range(self._size)] for j in range(self._size)]
        for ship in self.get_ships():
            s = (1, 0)
            if ship._tp == 2:
                s = (0, 1)
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
            s = (1, 0)
            if ship._tp == 2:
                s = (0, 1)
            for e in range(ship._length):
                x, y = ship.get_start_coords()
                temp_pole[x + e * s[0]][y + e * s[1]] = ship[e]
        tmp_tuple=tuple(tuple(x) for x in temp_pole)
        return tmp_tuple
        



# pole = GamePole(SIZE_GAME_POLE)
# pole.init()
# print(pole.get_pole())

# pole.show()
# print(pole.get_ships())

# pole.move_ships()

# print(pole.get_ships())
# pole.show()
# ------------------------------


class SeaBattle:
    ...

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
print('ooooooo')
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

pole_size_8 = GamePole(8)
pole_size_8.init()