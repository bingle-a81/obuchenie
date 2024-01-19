from random import randint


SIZE_GAME_POLE = 10


class Ship:
    ship_lst = []

    def __init__(self, length, x=None, y=None, tp=1) -> None:
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
            a = self._x + self._orient[0] * go
            b = self._y + self._orient[1] * go
            self.set_start_coords(a, b)
            # print(self.is_out_pole(SIZE_GAME_POLE))
            if self.is_out_pole(SIZE_GAME_POLE) == False:
                self.set_start_coords(-10, -10)
                if self.is_collide(a, b) == False:
                    self.set_start_coords(a, b)
                else:
                    self.set_start_coords(x1, y1)
                    return

            self.set_start_coords(x1, y1)

    # @classmethod
    def is_collide(self, a, b):
        lst = Ship._set_pole()
        for e in range(self._length):
            if lst[a + e * self._orient[0]][b + e * self._orient[1]] != 0:
                print(a + e * self._orient[0])
                return True
        return False

        # if all(
        #     lst[self._x + e * self._orient[0]][self._y + e * self._orient[1]] == 0
        #     for e in range(self._length)
        # ):

        # else:
        #     return True

    def is_out_pole(self, size):
        for e in range(self._length):
            if all(
                [
                    0 <= self._x + e * self._orient[0] < size,
                    0 <= self._y + e * self._orient[1] < size,
                ]
            ):
                return False
            else:
                return True

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
        # for i in range(self._size):
        #     for j in range(self._size):
        #         print(Ship._set_pole()[i][j], end=" ")
        #     print("")

    def get_pole(self):
        ...


pole = GamePole(SIZE_GAME_POLE)
pole.init()

pole.show()
print(pole.get_ships())

pole.move_ships()

print(pole.get_ships())
pole.show()
# ------------------------------


class SeaBattle:
    ...
