class  TriangleListIterator:
    i=0
    def __init__(self,lst) -> None:
        self.lst=lst


    def __iter__(self):
        return self

    def __next__(self):
        while self.i<len(self.lst):
            j=0
            while j<=self.i:   
                # print (self.lst[self.i][self.i] )  
                res=self.lst[self.i][j]     
                j+=1     
                yield(res )
            self.i+=1
            return 
        else:
            raise StopIteration


lst = [['x00', 'x01', 'x02'],
       ['x10', 'x11'],
       ['x20', 'x21', 'x22', 'x23', 'x24'],
       ['x30', 'x31', 'x32', 'x33']]

it = TriangleListIterator(lst)
# print(next(it))
# print(next(it))
# print(next(it))

for x in it:  # последовательный перебор всех элементов списка: x00, x10, x11, x20, ...
    print(x)

# it_iter = iter(it)
# x = next(it_iter)