class TupleLimit(tuple):
    def __new__(cls, *args, **kwargs):
        if len(args[0]) > args[1]:
            raise ValueError('число элементов коллекции превышает заданный предел')
        return super().__new__(cls, args[0])
        
    def __init__(self,lst,max) -> None:
         super().__init__()
         self.lst=lst


    def __str__(self) -> str:
        return ' '.join(str(float(x)) for x in self.lst)


digits = list(map(float, input().split()))  # эту строчку не менять (коллекцию digits также не менять)

try:
    print(TupleLimit(digits,2))
except ValueError as z:
    print(z)
