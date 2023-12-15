class Integer :
    def __init__(self,start_value) -> None:
        self.start_value=start_value

    @property
    def start_value(self):
        return self.__start_value
    @start_value.setter
    def start_value(self, val):
        if type(val)!=int:
            raise ValueError('должно быть целое число')
        self.__start_value = val

    def __str__(self) -> str:
        return str(self.start_value)



class Array:
    def __init__(self,max_length, cell=None) -> None:
        self.max_length=max_length
        self.cell=cell
        self.lst=[self.cell(0) for x in range(max_length)]


    def __getitem__(self,item):
        if not (0<=item<self.max_length):
            raise IndexError('неверный индекс для доступа к элементам массива')
        return self.lst[item].start_value

    def __setitem__(self,item,val):
        if not (0<=item<self.max_length):
            raise IndexError('неверный индекс для доступа к элементам массива')
        self.lst[item].start_value=val

    def __str__(self) -> str:
        return ' '.join([str(x) for x in self.lst])


a = Array(20, cell=Integer)

assert a[18] == 0, "начальные значения в ячейках массива (в объектах класса Integer) должны быть равны 0"

a = Array(2, cell=Integer)
a[0] = 1
a[1] = 2
assert str(a) == "1 2", "функция str(a) для объекта класса Array вернула неверное значение"
assert a[0] == 1 and a[1] == 2, "некорректно работает запись и/или считывание значений из массива по индексу"

try:
    a[1] = 2.5
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

    
try:
    a[100] = 25
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"