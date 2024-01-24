class Rect:
    def __init__(self, x, y, width, height) -> None:
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self.left = self._x
        self.right = self._x + self._width
        self.up = self._y
        self.bottom = self._y + self._height

    def __setattr__(self, __name: str, __value):
        if type(__value) not in (int, float):
            raise ValueError("некорректные координаты и параметры прямоугольника")
        if __name in ("_width", "_height") and __value <= 0:
            raise ValueError("некорректные координаты и параметры прямоугольника")
        return object.__setattr__(self, __name, __value)

    def is_collision(self, rect):
        if (
            self.right < rect.left
            or self.left > rect.right
            or self.up > rect.bottom
            or self.bottom < rect.up
        ):
            return True
        raise TypeError("прямоугольники пересекаются")


a = Rect(0, 2, 0, 20)

lst_rect = [Rect(0, 0, 5, 3), Rect(6, 0, 3, 5), Rect(3, 2, 4, 4), Rect(0, 8, 8, 1)]
lst_not_collision = [lst_rect[-1]]
print(lst_not_collision)
