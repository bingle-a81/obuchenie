import random

class Cell:
    def __init__(self,number:int=0, is_mine:bool=False,is_open:bool=False):
        self.number = number
        self.is_mine = is_mine
        self.is_open = is_open


        @property
        def number(self):
            return self.__number
        @number.setter
        def number(self, val):
            if type(val) not in (int,float):
                raise ValueError("недопустимое значение атрибута")
            self.__number = val

        @property
        def is_mine(self):
            return self.__is_mine
        @is_mine.setter
        def is_mine(self, val):
            if type(val)!= bool:
                raise ValueError("недопустимое значение атрибута")
            self.__is_mine = val

        @property
        def is_open(self):
            return self.__is_open
        @is_open.setter
        def is_open(self, val):
            if type(val)!= bool:
                raise ValueError("недопустимое значение атрибута")
            self.__is_open = val        

        def __bool__(self):
            return self.is_open


class GamePole:
    __isis=None
    def __new__(cls,*args,**kwargs) :
        if cls.__isis is None:
            cls.__isis=super().__new__(cls)
        return cls.__isis

    def __init__(self,N, M, total_mines) -> None:
        self.N=N
        self.M=M
        self.__pole_cells=[[Cell() for i in range(self.M)] for j in range(self.N)]
        self.pole=self.__pole_cells
        self.total_mines=total_mines

    @property
    def pole(self):
        return self.__pole
    @pole.setter
    def pole(self,val):
        self.__pole=self.__pole_cells
        # TODO property  проверка


    def init_pole(self):
        self.temp_pole=[[0 for i in range(self.M)] for j in range(self.N)]
        self.add_mines()
        for i in range(self.N):
            for j in range(self.M):
                    k=self.sum_around_mines(i,j)
                    if self.temp_pole[i][j]==1:
                        self.pole[i][j]=Cell(number=0, is_mine=True)
                    else:
                        self.pole[i][j]=Cell(number=k,is_mine=False) 

    def sum_around_mines(self,i,j):
        a=((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))
        b=sum([self.temp_pole[i+x[0]][j+x[1]] for x in a if 0<=i+x[0]<self.N and 0<=j+x[1]<self.M])
        return b                        

    def add_mines(self):
        k=0
        while k<self.total_mines:
            a,b=random.randint(0,self.N-1),random.randint(0,self.M-1)
            if self.temp_pole[a][b]==0:
                self.temp_pole[a][b]=1
                k+=1
            else:
                continue   

    def open_cell(self,i, j):
        # TODO  открывает ячейку с индексами
        '''В методе open_cell() необходимо проверять корректность индексов (i, j). 
        Если индексы указаны некорректно, то генерируется исключение командой:
            raise IndexError('некорректные индексы i, j клетки игрового поля')
        '''
        pass

    def show_pole(self):
        for i in range(self.N):
            for j in range(self.M):
                if self.pole[i][j].is_open==False:
                    print('#',end=' ')
                else:
                    if self.pole[i][j].is_mine:
                        print('*',end=' ')
                    else:
                        print(self.pole[i][j].number,end=' ')
            print('')




pole = GamePole(4, 8, 3)  # создается поле размерами 10x20 с общим числом мин 10
pole.init_pole()
if pole.pole[0][1]:
    pole.open_cell(0, 1)
if pole.pole[3][5]:
    pole.open_cell(3, 5)
pole.open_cell(30, 100)  # генерируется исключение IndexError
pole.show_pole()
