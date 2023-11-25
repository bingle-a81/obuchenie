from typing import Any


class Circle:
    def __init__(self,x, y, radius):
        self.x=x
        self.y=y
        self.radius=radius

    # @property
    # def x(self):
    #     return self.__x
    
    # @property
    # def y(self):
    #     return self.__y
    
    # @property
    # def radius(self):
    #     return  self.__radius
    
    def __setattr__(self, __name: str, __value) -> None:
        if __name =='radius' and __value<0  :
            raise ValueError('Radius cannot be negative')
        if __name in ('x', 'y', 'radius') and type(__value)  not in (int, float):
            raise TypeError("Неверный тип присваиваемых данных.")
        object.__setattr__(self,__name, __value)

    def __getattr__(self, __name: str):
        return False
    

circle = Circle(10.5, 7, 22)
circle.radius = 10 # прежнее значение не должно меняться, т.к. отрицательный радиус недопустим
x, y = circle.x, circle.y
res = circle.name # False, т.к. атрибут name не существует