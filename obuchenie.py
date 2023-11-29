class ghost:
    def __init__(self,a,):
     self.a = a 

    def __call__(self,z:int) :
        if type(z)==int:
            return self.a(z*5)
        else:
            return f'type err'

@ghost
def ssum(t:int):
    t=t+1
    return t



f=ssum(10)
print(f)