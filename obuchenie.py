class Triangle:
    def __init__(self,a, b, c) -> None:  
        self.__a=self.__b=self.__c=None      
        self.a=a
        self.b=b
        self.c=c

    def __is_triangle(self):
        if all([self.a is not None,self.b is not None,self.c is not None]):
            if any([self.a > self.b+self.c,  self.b > self.a+self.c, self.c > self.a+ self.b]):
                raise ValueError("с указанными длинами нельзя образовать треугольник")
        return 
    
    @property
    def a(self):
        return self.__a
    @a.setter
    def a(self, val):
        self.__check(val)
        if all([self.__b is not None,self.__c is not None]):
            if any([val > self.b+self.c,  self.b > val+self.c, self.c > val+ self.b]):
                raise ValueError("с указанными длинами нельзя образовать треугольник")
        self.__a = val        

    @property
    def b(self):
        return self.__b
    @b.setter
    def b(self, val):
        self.__check(val)   
        if all([self.a is not None,self.c is not None]):
            if any([self.a > val+self.c,  val > self.a+self.c, self.c > self.a+ val]):
                raise ValueError("с указанными длинами нельзя образовать треугольник")
        self.__b = val


    @property
    def c(self):
        return self.__c
    @c.setter
    def c(self, val):
        self.__check(val)    
        if all([self.a is not None,self.b is not None]):
            if any([self.a > self.b+val,  self.b > self.a+val, val > self.a+ self.b]):
                raise ValueError("с указанными длинами нельзя образовать треугольник")            
        self.__c = val
        self.__is_triangle()

    def __len__(self):
        return int(self.a+self.b+self.c)

    def __check(self,__v):
        if type(__v) not in (int,float) or __v<=0:
            raise ValueError("длины сторон треугольника должны быть положительными числами")
        return True

    def __call__(self) :
        p=(self.a+self.b+self.c)/2
        res = (p * (p-self.a) * (p-self.b) * (p-self.c))**0.5
        return res


tr = Triangle(5, 4, 3)
try:
    tr = Triangle(-15,5,6)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueEr"   

print(tr.a)
assert tr.a == 5 and tr.b == 4 and tr.c == 3, "дескрипторы вернули неверные значения"
print(len(tr))
# quit(-1)
try:
    tr = Triangle(-5, 4, 3)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"


try:
    tr = Triangle(10, 1, 1)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

    
tr = Triangle(5, 4, 3)
assert len(tr) == 12, "функция len вернула неверное значение"
assert 5.9 < tr() < 6.1, "метод __call__ вернул неверное значение"