from random import randint

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