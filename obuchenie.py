import random

class Cell:
    def __init__(self,value=0) -> None:
        self.value=value
    def __bool__(self,):
        return True if self.value==0 else False

class TicTacToe:

    FREE_CELL = 0      # свободная клетка
    HUMAN_X = 1        # крестик (игрок - человек)
    COMPUTER_O = 2     # нолик (игрок - компьютер)

    _isictance=None

    def __new__(cls,*args,**kwargs) :
        if cls._isictance is None:
            cls._isictance=super().__new__(cls)
        return cls._isictance
    
    def __init__(self,is_human_win=False,is_computer_win=False,is_draw=False):
        self.bisy_cell=0
        self.is_human_win=is_human_win
        self.is_computer_win=is_computer_win
        self.is_draw=is_draw
        self.pole=[]
        self.init()

    def init(self) -> None:
        self.pole=tuple(tuple(Cell() for x in range(3)) for x in range(3) )
        self.is_human_win=False
        self.is_computer_win=False
        self.is_draw=False

    @property
    def is_human_win(self):
        return self.__is_human_win
    @is_human_win.setter
    def is_human_win(self, val):
        self.__is_human_win = val
    @property
    def is_computer_win(self):
        return self.__is_computer_win
    @is_computer_win.setter
    def is_computer_win(self, val):
        self.__is_computer_win = val
    @property
    def is_draw(self):
        return self.__is_draw
    @is_draw.setter
    def is_draw(self, val):
        self.__is_draw = val

    def check_win(self):
        temp_ls=[x for row in self.pole for x in row]
        lk=(slice(0,3),slice(3,6),slice(6,None),slice(0,None,3),slice(1,None,3),slice(2,None,3),slice(0,None,4),slice(2,8,2))
        for x in lk:
            if all(y.value ==self.HUMAN_X for y in temp_ls[x] ):
                self.is_human_win=True
                return False
            elif all(y.value ==self.COMPUTER_O for y in temp_ls[x] ):
                self.is_computer_win=True
                return False
        return True

    def _check_bisy_cells(self,):
        if self.bisy_cell>8 :
            self.is_draw=True
            return True
        else:
            return False


    def _check(self,item:list):
        if not all([0<=item[0]<3,0<=item[1]<3,type(item[0])==int,type(item[1])==int]):
            raise IndexError('некорректно указанные индексы')
        return

    def __getitem__(self,item):
        self._check(item)
        return self.pole[item[0]][item[1]].value

    def __setitem__(self,item,val):
        self._check(item) 
        if bool(self.pole[item[0]][item[1]])==False:
            raise ValueError('клетка уже занята')        
        self.pole[item[0]][item[1]].value = val
        self.check_win()
    
    def show(self):
        for i in range(3):
            for j in range(3):
                print(self.pole[i][j].value,end=' ')
            print('')      

    def __bool__(self,):
        if self.check_win()==False and self._check_bisy_cells()==True:
            return False
        elif self._check_bisy_cells()==False:
            return True
        else:
            return True

    def human_go(self):
        if self._check_bisy_cells()==False:
            flag=True
        else:
            flag=False
        while flag:         
            i,j=map(int,input().split())
            
            if not all([0<=i<3,0<=j<3]):
                print('введи правильно еще раз')
                continue 
            else:
                if (self.pole[i][j]):
                    self.pole[i][j].value=self.HUMAN_X
                    self.bisy_cell+=1
                    flag=False
                else:
                    print('значение есть')
                    continue 


    def computer_go(self):  
        if self._check_bisy_cells()==False:
            flag=True
        else:
            flag=False
        while flag:         
            i=random.randint(0,2)
            j=random.randint(0,2)
            if (self.pole[i][j]):               
                self.pole[i][j].value=self.COMPUTER_O
                self.bisy_cell+=1
                flag=False



cell = Cell()
assert cell.value == 0, "начальное значение атрибута value объекта класса Cell должно быть равно 0"
assert bool(cell), "функция bool для объекта класса Cell вернула неверное значение"
cell.value = 1
assert bool(cell) == False, "функция bool для объекта класса Cell вернула неверное значение"

assert hasattr(TicTacToe, 'show') and hasattr(TicTacToe, 'human_go') and hasattr(TicTacToe, 'computer_go'), "класс TicTacToe должен иметь методы show, human_go, computer_go"

game = TicTacToe()

assert bool(game), "функция bool вернула неверное значения для объекта класса TicTacToe"
assert game[0, 0] == 0 and game[2, 2] == 0, "неверные значения ячеек, взятые по индексам"
game[1, 1] = TicTacToe.HUMAN_X
assert game[1, 1] == TicTacToe.HUMAN_X, "неверно работает оператор присваивания нового значения в ячейку игрового поля"

game[0, 0] = TicTacToe.COMPUTER_O
assert game[0, 0] == TicTacToe.COMPUTER_O, "неверно работает оператор присваивания нового значения в ячейку игрового поля"

game.init()
assert game[0, 0] == TicTacToe.FREE_CELL and game[1, 1] == TicTacToe.FREE_CELL, "при инициализации игрового поля все клетки должны принимать значение из атрибута FREE_CELL"

try:
    game[3, 0] = 4
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

game.init()
assert game.is_human_win == False and game.is_computer_win == False and game.is_draw == False, "при инициализации игры атрибуты is_human_win, is_computer_win, is_draw должны быть равны False, возможно не пересчитывается статус игры при вызове метода init()"

game[0, 0] = TicTacToe.HUMAN_X
game[1, 1] = TicTacToe.HUMAN_X
game[2, 2] = TicTacToe.HUMAN_X


assert game.is_human_win and game.is_computer_win == False and game.is_draw == False, "некорректно пересчитываются атрибуты is_human_win, is_computer_win, is_draw. Возможно не пересчитывается статус игры в момент присвоения новых значения по индексам: game[i, j] = value"

game.init()
game[0, 0] = TicTacToe.COMPUTER_O
game[1, 0] = TicTacToe.COMPUTER_O
game[2, 0] = TicTacToe.COMPUTER_O
assert game.is_human_win == False and game.is_computer_win and game.is_draw == False, "некорректно пересчитываются атрибуты is_human_win, is_computer_win, is_draw. Возможно не пересчитывается статус игры в момент присвоения новых значения по индексам: game[i, j] = value"
