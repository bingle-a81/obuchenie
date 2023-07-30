<<<<<<< HEAD
<<<<<<< HEAD
import sec1
import fr



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
