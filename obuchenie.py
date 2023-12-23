class Matrix:
    def __init__(self,*args) -> None:
        if len(args)==1:
            self._check_list(*args)
            self.ls=list(*args)
        else:                        
            self.rows=args[0]
            self.cols=args[1]
            self.fill_value=args[2]
            self.ls=[[0]*self.cols]*self.rows
            for i in range(self.rows):
                for j in range(self.cols):
                    self.ls[i][j]=self.fill_value


    @property
    def rows(self):
        return self.__rows
    @rows.setter
    def rows(self, __value):
        if type(__value) !=int:
            raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')      
        self.__rows = __value

    @property
    def cols(self):
        return self.__cols
    @cols.setter
    def cols(self, __value):
        if type(__value) !=int:
            raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')        
        self.__cols = __value

    @property
    def fill_value(self):
        return self.__fill_value
    @fill_value.setter
    def fill_value(self, __value):
        if type(__value) not in (int,float):
            raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')             
        self.__fill_value = __value

    def _check_list(self,ls):
        if len(set(len(x) for x in ls))!=1 or any(type(x) not in (int,float) for row in ls for x in row):
            raise TypeError('список должен быть прямоугольным, состоящим из чисел')
    
    def _check_index(self,item:list):
        if not all(type(x)==int for x in item):
            raise IndexError('недопустимые значения индексов')
        if not all([0<=item[0]<len(self.ls), 0<=item[1]<len(self.ls[0])]):
            raise IndexError('недопустимые значения индексов')

    def __getitem__(self,item):
        self._check_index(item)
        return self.ls[item[0]][item[1]]
    
    def __setitem__(self,item,val):
        self._check_index(item=item)
        if type(val) not in (int,float):
            raise TypeError('значения матрицы должны быть числами')
        self.ls[item[0]][item[1]]=val

    def __add__(self,other):
        temp=self.ls.copy()
        if type(other)==int:
            for i in range(len(self.ls)):
                for j in range(len(self.ls)):
                    temp[i][j]=self.ls[i][j]+other
        else:
            # self._check_list(other)

            if len(self.ls)!=len(other.ls) or len(self.ls[0])!=len(other.ls[0]):
                raise ValueError('операции возможны только с матрицами равных размеров')
            for i in range(len(self.ls)):
                for j in range(len(self.ls)):
                    temp[i][j]=temp[i][j]+other.ls[i][j]  
                    print(temp[i][j],self.ls[i][j])         
        return Matrix



mt = Matrix([[1, 2], [3, 4]])
matrix = Matrix(4, 5, 0)

list2D = [[1, 2], [3, 4], [5, 6, 7]]
try:
    st = Matrix(list2D)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError для не прямоугольного списка в конструкторе Matrix"

list2D = [[1, []], [3, 4], [5, 6]]
try:
    st = Matrix(list2D)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError для списка не из чисел в конструкторе Matrix"

try:
    st = Matrix('1', 2, 0)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError для не числовых аргументов в конструкторе Matrix"

list2D = [[1, 2], [3, 4], [5, 6]]
matrix = Matrix(list2D)
assert matrix[2, 1] == 6, "неверно отработал конструктор или __getitem__"

matrix = Matrix(4, 5, 10)
assert matrix[3, 4] == 10, "неверно отработал конструктор или __getitem__"

try:
    v = matrix[3, -1]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

try:
    v = matrix['0', 4]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

matrix[0, 0] = 7
assert matrix[0, 0] == 7, "неверно отработал __setitem__"

try:
    matrix[0, 0] = 'a'
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError в __setitem__"

m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[1, 1], [1, 1], [1, 1]])

try:
    matrix = m1 + m2
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при сложении матриц разных размеров"

m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[1, 1], [1, 1]])
matrix = m1 + m2
print(matrix.ls)
assert isinstance(matrix, Matrix), "операция сложения матриц должна возвращать экземпляр класса Matrix"
assert matrix[1, 1] == 5, "неверно отработала операция сложения матриц"
assert m1[1, 1] == 4 and m1[0, 1] == 2 and m2[1, 1] == 1 \
       and m2[0, 0] == 1, "исходные матрицы не должны меняться при операции сложения"

m1 = Matrix(2, 2, 1)
id_m1_old = id(m1)
m2 = Matrix(2, 2, 1)
m1 = m1 + m2
id_m1_new = id(m1)
assert id_m1_old != id_m1_new, "в результате операции сложения должен создаваться НОВЫЙ экземпляр класса Matrix"

matrix = Matrix(2, 2, 0)
m = matrix + 10
assert matrix[0, 0] == matrix[1, 1] == 0, "исходные матрицa не должна меняться при операции сложения c числом"
assert m[0, 0] == 10, "неверно отработала операция сложения матрицы с числом"

m1 = Matrix(2, 2, 1)
m2 = Matrix([[0, 1], [1, 0]])
identity_matrix = m1 - m2  # должна получиться единичная матрица
assert m1[0, 0] == 1 and m1[1, 1] == 1 and m2[0, 0] == 0 \
       and m2[0, 1] == 1, "исходные матрицы не должны меняться при операции вычитания"
assert identity_matrix[0, 0] == 1 and identity_matrix[1, 1] == 1, "неверно отработала операция вычитания матриц"

matrix = Matrix(2, 2, 1)
m = matrix - 1
assert matrix[0, 0] == matrix[1, 1] == 1, "исходные матрицa не должна меняться при операции вычитания c числом"
assert m[0, 0] == m[1, 1] == 0, "неверно отработала операция вычитания числа из матрицы"