import random

class Cell:
    def __init__(self,around_mines:int=0, mine:bool=False,fl_open:bool=False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open=fl_open

class GamePole:
    isis=None
    def __new__(cls,*args,**kwargs) :
        if cls.isis==None:
            cls.isis=super().__new__(cls)
        return cls.isis
        
    def __init__(self,N, M, total_mines):
        self.N=N
        self.M=M
        self.__pole_cells=[[Cell() for i in range(self.N)] for j in range(self.N)]
        self.pole=self.__pole_cells


    @property
    def pole(self):
        return self.__pole
