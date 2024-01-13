class Note:
    NOTE_LIST = ("до", "ре", "ми", "фа", "соль", "ля", "си")

    def __init__(self, name, ton) -> None:
        self._name = name
        self._ton = ton

    @property
    def _name(self):
        return self.__name

    @_name.setter
    def _name(self, __value):
        if __value not in self.NOTE_LIST:
            raise ValueError("недопустимое значение аргумента")
        self.__name = __value

    @property
    def _ton(self):
        return self.__ton

    @_ton.setter
    def _ton(self, __value):
        if type(__value) != int or __value not in (-1, 0, 1):
            raise ValueError("недопустимое значение аргумента")
        self.__ton = __value


class Notes:
    __slots__ = ("_do", "_re", "_mi", "_fa", "_solt", "_la", "_si")
    NOTE_LIST = ("до", "ре", "ми", "фа", "соль", "ля", "си")
    __isictance = None

    def __new__(cls, *args, **kwargs):
        if cls.__isictance is None:
            cls.__isictance = super().__new__(cls, *args, **kwargs)
        return cls.__isictance

    def __init__(self) -> None:
        for k, v in zip(self.__slots__, self.NOTE_LIST):
            setattr(self, k, Note(v, 0))

    def __getitem__(self, item):
        if not 0 <= item < 7:
            raise IndexError("недопустимый индекс")
        return getattr(self, self.__slots__[item])


notes = Notes()
nota = notes[2]  # ссылка на ноту ми
print(nota._ton)
notes[6]._ton = 1  # изменение тональности ноты фа
print(notes[6]._ton)
n = Note("ми", 0)
print(n._ton)
