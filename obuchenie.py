
class Dimensions:
    def __init__(self,a,b,c,):
        self.a = a
        self.b = b
        self.c = c
    
    def __getattribute__(self, __name: str) :
        return  object.__getattribute__(self,__name)
    
    def __setattr__(self, __name: str, __value) :
        if __name in ('a','b','c') and __value<=0:
            raise ValueError("габаритные размеры должны быть положительными числами")
        object.__setattr__(self,__name,__value)

    def __hash__(self) -> int:
        return hash((self.a,self.b,self.c))
    
    def __repr__(self) -> str:
        return f'{hash(self)}'


a=input()

lst_dims=[Dimensions(*list(map(lambda x:float(x.strip()),y.split()))) for y in a.split(';')]

lst_dims.sort(key=hash)
print(lst_dims)