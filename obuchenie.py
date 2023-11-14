import random

class Cell:
    def __init__(self,around_mines:int, mine:int):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open=True


class GamePole:
    def __init__(self,N:int,M:int):
        self.N=N
        self.M=M
        self.pole=[['#' for i in range(self.N)] for j in range(self.N)]
        for i in range(self.M):
            self.pole[random.randint(0,self.N-1)][random.randint(0,self.N-1)]='*'
    
       
    
    def show(self):
        for i in range(self.N):
            for j in range(self.N):
                print(self.pole[i][j],end=' ')
            print('')


N=10
M=12
pole_game=GamePole(N,M)
pole_game.show()