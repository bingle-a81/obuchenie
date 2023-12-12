class Diskr:
    @classmethod
    def _check(cls,val):
        if type(val) not in (int,float) or val<=0:
            raise ValueError("длины сторон треугольника должны быть положительными числами")
        return True


    def __set_name__(self, owner, name):
        self.name = '_'+name
 
    def __get__(self, instance, owner):
        return getattr(instance, self.name,None)
 
    def __set__(self, instance, value):
        self._check(value)
        if len(instance.__dict__)>1:
            a=instance.__dict__.get('_a')
            b=instance.__dict__.get('_b')
            if any([a > value+b,  value > a+b, b > a+ value]):
                raise ValueError("с указанными длинами нельзя образовать треугольник")
        setattr(instance, self.name, value)


class Triangle:
    a=Diskr()
    b=Diskr()
    c=Diskr()

    def __init__(self,a, b, c) -> None:   
        self.a=a
        self.b=b
        self.c=c

    def __len__(self):
        return int(self.a+self.b+self.c)

    def __call__(self) :
        p=(self.a+self.b+self.c)/2
        res = (p * (p-self.a) * (p-self.b) * (p-self.c))**0.5
        return res


# tr = Triangle(15, 4, 3)
# print(tr.__dict__)
# quit(-1)
# tr = Triangle(15,5,6)

try:
    tr = Triangle(15,5,6)
except ValueError:
    assert True
    # print(tr.a)
else:
    assert False, "не сгенерировалось исключение ValueEr"   

assert tr.a == 5 and tr.b == 4 and tr.c == 3, "дескрипторы вернули неверные значения"

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