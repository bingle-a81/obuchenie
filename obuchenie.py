class Cell:
    def __init__(self,data=0 ) -> None:
        self.data =data 

    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, val):
        self.__data = val


class TableValues :
    def __init__(self,rows, cols, type_data=int) -> None:
        self.rows=rows
        self.cols=cols
        self.type_data=type_data
        self.table=tuple(tuple(Cell() for x in range(cols))for x in range(rows))

    def __getitem__(self,item):
        if not any((0<=item[0]<self.rows,0<=item[1]<self.cols)):
            raise IndexError('неверный индекс')
        return self.table[item[0]][item[1]].data

    def __setitem__(self,item,val):
        if not any((0<=item[0]<self.rows,0<=item[1]<self.cols)):
            raise IndexError('неверный индекс')
        if type(val)!=self.type_data:
            raise TypeError('неверный тип присваиваемых данных')
        self.table[item[0]][item[1]].data=val

    def __iter__(self):
        try:
            for row in self.table:
                yield (x.data for x in row)           
        except StopIteration:
            print('st')
        return self


tb = TableValues(3, 2)
n = m = 0
for row in tb:
    n += 1
    for value in row:
        m += 1
        assert type(value) == int and value == 0, "при переборе объекта класса TableValues с помощью вложенных циклов for, должен сначала возвращаться итератор для строк, а затем, этот итератор должен возвращать целые числа (значения соответствующих ячеек)"
        
assert n > 1 and m > 1, "неверно отработали вложенные циклы для перебора ячеек таблицы"


tb[0, 0] = 10
assert tb[0, 0] == 10, "не работает запись нового значения в ячейку таблицы"


try:
    tb[2, 0] = 5.2
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError"


try:
    a = tb[2, 4]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"
