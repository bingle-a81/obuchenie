class Thing:
    def __init__(self,name,mass,):
        self.name = name.lower()
        self.mass = mass
        
    def __eq__(self, name:str) -> bool:
        if isinstance(name,Thing):
            return self.name.lower()==name.name.lower()
        else:
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
        lo1=__value.ls[:]
        for i,x in enumerate(self.ls):
            print(x.name)
            for y in lo1:
                if y==x:
                    lo1.remove(y)
                else

                    
        return len(lo1)==0

b1 = Box()
b2 = Box()

b1.add_thing(Thing('мел', 100))
b1.add_thing(Thing('Тряпка', 200))
b1.add_thing(Thing('Тряпка', 200))
b1.add_thing(Thing('доска', 2000))

b2.add_thing(Thing('тряпка', 200))
b2.add_thing(Thing('Мел', 100))
# b2.add_thing(Thing('доска', 2000))
b2.add_thing(Thing('доска', 2000))

res = b1 == b2 # True
print(res)