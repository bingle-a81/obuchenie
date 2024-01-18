from random import randint

SIZE_GAME_POLE = 10


class Ship:
    def __init__(self, length, x=None, y=None, tp=1) -> None:
        self._x = x
        self._y = y
        self._tp = tp
        self._length = length
        self._is_move = True
        self._cells = [1 for x in range(self._length)]
        self._points = []

    def set_start_coords(self, x, y):
        self._x = x
        self._y = y

    def get_start_coords(self):
        return (self._x, self._y)

    def move(self, go):
        ...

    def is_collide(self, ship):
        ...

    def is_out_pole(self, size):
        ...

    def __getitem__(self, item):
        ...

    def __setitem__(self, item, val):
        ...

    def __repr__(self) -> str:
        return f"{self._length}:({self._x},{self._y}),{self._tp}"


# ---------------------


class GamePole:
    SHIPS = [
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

    def __init__(self, size) -> None:
        self._size = size
        self._ships = []

    def init(self):
        self.temp_pole = [[0 for i in range(self._size)] for j in range(self._size)]
        for ship in self.SHIPS:
            self._ships.append(self._add_ships(ship))

    def _check_point(self, x, y):
        if all([0 <= x < self._size, 0 <= y < self._size]) and (
            self.temp_pole[x][y] == 0
        ):
            return True
        return False

    def _add_ships(self, ship):
        s = (1, 0)
        if ship._tp == 2:
            s = (0, 1)
        while True:
            a, b = randint(0, self._size), randint(0, self._size)
            if self._check_point(a + ship._length * s[0], b + ship._length * s[1]):
                return Ship(length=ship._length, x=a, y=b, tp=ship._tp)

    # def _ship_constructor(self, x, y, ship: Ship) -> Ship:
    #     s = (1, 0)
    #     if ship._tp == 2:
    #         s = (0, 1)
    #     for e in range(ship._length):
    #         self.temp_pole[x + e * s[0]][y + e * s[1]] = 1
    #     return Ship(ship._length, x=x, y=y, tp=ship._tp)

    def get_ships(self):
        return self._ships

    def move_ships(self):
        ...

    def show(self):
        for i in range(self._size):
            for j in range(self._size):
                print(self.temp_pole[i][j], end=" ")
            print("")

    def get_pole(self):
        ...


pole = GamePole(SIZE_GAME_POLE)
pole.init()
# pole._add_ships()
pole.show()
print(pole.get_ships())

# ------------------------------


class SeaBattle:
    ...
