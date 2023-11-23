class Bag:
    def __init__(self, max_weight):
        self.__max_weight=0
        self.max_weight = max_weight
        self.__things = []

    @property
    def max_weight(self):
        return self.__max_weight
    
    @max_weight.setter
    def max_weight(self, value):
        if type(value) == int:
            self.__max_weight = value

    @property
    def things(self):
        return self.__things
    
    def add_thing(self, thing):
        self.__things.append(thing)
        self.max_weight += thing.weight