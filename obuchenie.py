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

class GamePole:
    def __init__(self,kol_cell,kol_mine) -> None:
        self.kol_cell=kol_cell
        self.kol_mine=kol_mine
        self.pole=[[Cell() for x in range(self.kol_cell)] for y in range(self.kol_cell)]
        self.inicial()

    def inicial(self) :
        a=0
        while a <= self.kol_mine:
            i=randint(0,self.kol_cell-1)
            j=randint(0,self.kol_cell-1)
            if self.pole[i][j].mine==True:
                continue
            self.pole[i][j].mine=True
            a+=1
        indx=(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
        for x in range(self.kol_cell):
            for y in range(self.kol_cell):
                if self.pole[x][y].mine==False:
                    mines=sum(self.pole[x+i][y+j].mine for i,j in indx if (0<=x+i<self.kol_cell) and (0<=j+y<self.kol_cell))
                    self.pole[x][y].around_mines=mines

    def show(self):
        for row in self.pole:
            print(*map(lambda x:'%' if x.fl_open==False else x.around_mines if x.mine==False else '*',row))

d=GamePole(30,90)
d.show()
>>>>>>> 33768e2 (4)
