class  IterColumn:

    def __init__(self,lst,column) -> None:
        self.lst=lst
        self.column=column
        self.i=0
        self.temp=list(map(list,zip(*self.lst)))


    def __iter__(self):
        try:
            for x in self.temp[self.column]:
                yield(x )
                
        except StopIteration:
            print('st')

    



lst = [['x00', 'x01', 'x02'],
       ['x10', 'x11', 'x12'],
       ['x20', 'x21', 'x22'],
       ['x30', 'x31', 'x32']]

it = IterColumn(lst, 1)
for x in it:  # последовательный перебор всех элементов столбца списка: x12, x22, ..., xM2
    print(x)

it_iter = iter(it)
x = next(it_iter)