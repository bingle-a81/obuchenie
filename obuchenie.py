class Thing:
    def __init__(self,name, weight):
        self.__name=''
        self.__weight=0
        self.name = name
        self.weight = weight

    @property
    def name(self): 
        return self.__name
    
    @name.setter
    def name(self, value):
        if type(value) == str:
            self.__name = value
    
    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if type(value) in (int,float):
            self.__weight = value    


class Bag:
    def __init__(self, max_weight):
        self.__max_weight=0
        self.max_weight = max_weight
        self.__things = []
        self._weight=0

    @property
    def max_weight(self):
        return self.__max_weight
    
    @max_weight.setter
    def max_weight(self, value):
        if type(value) in (int,float):
            self.__max_weight = value

    @property
    def things(self):
        return self.__things

    
    def add_thing(self, thing:Thing):
        a= self._weight + thing.weight
        if a < self.max_weight:
            self._weight += thing.weight      
            self.__things.append(thing)


    def remove_thing(self, indx):
        self._weight -= self.__things[indx].weight
        self.__things.pop(indx)

    def get_total_weight(self):
        return self._weight


bag = Bag(1000)
bag.add_thing(Thing("Книга по Python", 100))
bag.add_thing(Thing("Котелок", 500))
bag.add_thing(Thing("Спички", 20))
bag.add_thing(Thing("Бумага", 100))
w = bag.get_total_weight()
print(w)
for t in bag.things:
    print(f"{t.name}: {t.weight}")        