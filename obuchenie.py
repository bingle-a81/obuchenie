class Thing:
    def __init__(self,name,mass,):
        self.name = name
        self.mass = mass
        
    def __eq__(self, name:str) -> bool:
        return self.name==name
    
    # def __ne__(self, name:str) -> bool:
    #     return self.name!=name



class Box:
    def __init__(self) -> None:
        self.ls=[]

    def add_thing(self, obj) :
        self.ls.append(obj)

    def get_things(self) :
        return self.ls
    
    def __eq__(self, __value) -> bool:
        lo=self.ls[:]
        for x in lo:
            for y in __value.ls:
                if x==y:
                    lo.remove(x)
        return len(lo)==0


b1 = Box()
b2 = Box()

b1.add_thing(Thing('мел', 100))
b1.add_thing(Thing('тряпка', 200))
b1.add_thing(Thing('доска', 2000))

b2.add_thing(Thing('тряпка', 200))
b2.add_thing(Thing('мел', 100))
b2.add_thing(Thing('доска', 2000))

res = b1 == b2 # True
print(res)