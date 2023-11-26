class Circle:
    def __init__(self,x, y, radius):
        # self.__x=self.__y=self.__radius=0
        self.__x=x
        self.__y=y
        self.__radius=radius

    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, value):
        self.__x=value

    
    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, value):
        self.__y=value
    
    @property
    def radius(self):
        return  self.__radius
    
    @radius.setter
    def radius(self, value):
        self.__radius=value
    


    def __setattr__(self, key, value):
        print(f'setattr',key)
        if not isinstance(value, (int, float)):
            raise TypeError("Неверный тип присваиваемых данных.")
        else:
            if key == '_Circle__x':
                object.__setattr__(self, key, value)
            elif key == '_Circle__y':
                object.__setattr__(self, key, value)
            elif key == '_Circle__radius' and value > 0:
                object.__setattr__(self, key, value)
            else:
                print('porn',self.__dict__)
                pass

    def __getattr__(self, item):
        return False
        
cr = Circle(20, 7, 22)
cr1 = Circle(20, 7, 22)
cr.x=50
print(cr.__dict__)
print(cr1.__dict__)
quit(-1)

assert type(Circle.x) == property and type(Circle.y) == property and type(Circle.radius) == property, "в классе Circle должны быть объявлены объекты-свойства x, y и radius"

try:
    cr = Circle(20, '7', 22)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError при инициализации объекта с недопустимыми аргументами"

cr = Circle(20, 7, 22)
assert cr.x == 20 and cr.y == 7 and cr.radius == 22, "объекты-свойства x, y и radius вернули неверные значения"

cr.radius = -10 # прежнее значение не должно меняться, т.к. отрицательный радиус недопустим
assert cr.radius == 22, "при присваивании некорректного значения, прежнее значение изменилось"

x, y = cr.x, cr.y
assert x == 20 and y == 7, "объекты-свойства x, y вернули некорректные значения"
assert cr.name == False, "при обращении к несуществующему атрибуту должно возвращаться значение False"

try:
    cr.x = '20'
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError"
    
cr.y = 7.8
cr.radius = 10.6
