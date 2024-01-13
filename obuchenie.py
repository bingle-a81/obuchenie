class Note:
    NOTE_LIST = ("до", "ре", "ми", "фа", "соль", "ля", "си")

    def __init__(self, name, ton) -> None:
        self._name = name
        self._ton = ton

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, __value):
        if __value not in self.NOTE_LIST:
            raise ValueError("недопустимое значение аргумента")
        self.__name = __value

    @property
    def ton(self):
        return self.__ton

    @ton.setter
    def ton(self, __value):
        if type(__value) != int and __value not in range(-1, 1):
            raise ValueError("недопустимое значение аргумента")
        self.__ton = __value


class Notes:
    __slots__ = ("_do", "_re", "_mi", "_fa", "_solt", "_la", "_si")
    __isictance = None

    def __new__(cls, *args, **kwargs):
        if cls.__isictance is None:
            cls.__isictance = super().__new__(cls, *args, **kwargs)
        return cls.__isictance

    def __getitem__(self, item):
        if not 0 <= item < 6:
            raise IndexError("недопустимый индекс")
        return getattr(self, self.__slots__[item])
