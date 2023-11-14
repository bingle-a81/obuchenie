<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
import sec1
import fr

<<<<<<< HEAD


if __name__ == '__main__':
    sec1.d()

=======
a =int(input())
b =int(input())
n =int(input())
=======
class Table:
    def __init__(self,name,price):
        self.name=name
        self.price=price
>>>>>>> 5a6de11 (88)

class TV:
    def __init__(self,name,price):
        self.name=name
        self.price=price

class Notebook:
    def __init__(self,name,price):
        self.name=name
        self.price=price

class Cup:
    def __init__(self,name,price):
        self.name=name
        self.price=price

class Cart:
    def __init__(self,goods=[]) -> None:
        self.goods=goods

    def add(self,gd)    :
        self.goods.append(gd)

    def remove(self,indx:int):
        if indx<=len(self.goods):
            self.goods.pop(indx)

    def get_list(self):
        return [f'{x.name}: {x.price}' for x in self.goods ]



cart = Cart()
        
tv1 = TV("samsung", 1111)
tv2 = TV("LG", 1234)
table = Table("ikea", 2345)
n1= Notebook("msi", 5433)
n2 = Notebook("apple", 542)
c = Cup("keepcup", 43)

<<<<<<< HEAD
print(s//3600,s%3600//60,s%60)
>>>>>>> 3c6fd4b (2)
=======
cart.add(tv1)
cart.add(tv2)
cart.add(table)
cart.add(n1)
cart.add(n2)
cart.add(c)
>>>>>>> 5a6de11 (88)
=======
class Cell:
    def __init__(self,around_mines=0, mine=False) -> None:
        self.around_mines=around_mines
        self.mine=mine
        self.fl_open=True
=======
from string import ascii_lowercase, digits

CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
CHARS_CORRECT = CHARS + CHARS.upper() + digits
>>>>>>> abe962b (3w)

class TextInput:
    
    def __init__(self,name,size=10,):
        self.name = name
        self.size = size
        if not (self.check_name(self.name) and 3<self.size<50):
            raise ValueError("некорректное поле name")

    def get_html(self):
        return f"<p class='login'>{self.name}: <input type='text' size={self.size} />"
    
    @classmethod
    def check_name(cls, name):
        if not all(x for x in name if x in CHARS_CORRECT):
            return

    

<<<<<<< HEAD
d=GamePole(30,90)
d.show()
>>>>>>> 33768e2 (4)
=======
class PasswordInput:

    def __init__(self,name,size=10,):
        self.name = name
        self.size = size

    def get_html(self):
        return f"<p class='password'>{self.name}: <input type='text' size={self.size} />"

# здесь объявляйте классы TextInput и PasswordInput
=======
class ListObject:
    def __init__(self,next_obj,data):
        self.next_obj = next_obj
        self.data = data

    def link(self,obj):
        self.next_obj = obj
>>>>>>> 243e4b7 (rrr)


lst_in = ['1. Первые шаги в ООП',
          '1.1 Как правильно проходить этот курс',
          '1.2 Концепция ООП простыми словами',
          '1.3 Классы и объекты. Атрибуты классов и объектов',
          '1.4 Методы классов. Параметр self',
          '1.5 Инициализатор init и финализатор del',
          '1.6 Магический метод new. Пример паттерна Singleton',
          '1.7 Методы класса (classmethod) и статические методы (staticmethod)']

head_obj=ListObject(None,lst_in[0])

for i in range(1,len(lst_in)):
    ListObject(head_obj,lst_in[i])

<<<<<<< HEAD
# эти строчки не менять
login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
html = login.render_template()
>>>>>>> abe962b (3w)
=======
>>>>>>> 243e4b7 (rrr)
