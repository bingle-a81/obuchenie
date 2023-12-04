class MaxPooling:
    def __init__(self,step=(2, 2), size=(2,2)) -> None:
        self.step=step
        self.size=size

    def __check(self,matrix):
        if not isinstance(matrix, list) or not all([len(row)==len(matrix[0]) for row in matrix]) or len(matrix) != len(matrix[0]):
            raise ValueError("Неверный формат для первого параметра matrix.")  
        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                if type(matrix[i][j]) not in (int,float):
                    raise ValueError("Неверный формат для первого параметра matrix.")  



    def __call__(self, matrix) :
        self.__check(matrix)
        rows = len(matrix)
        cols = len(matrix[0]) if rows > 0 else 0

        # Размер выходного массива
        rows = len(matrix)
        cols = len(matrix[0]) if rows > 0 else 0

        # Размер выходного массива
        output_rows = (rows - self.size[0]) // self.step[0] + 1
        output_cols = (cols - self.size[1]) // self.step[1] + 1

        # Создаем выходной массив
        res = [[0] * output_cols for _ in range(output_rows)]

        for i in range(output_rows):
            for j in range(output_cols):
                window = [matrix[i * self.step[0] + di][j * self.step[0]+ dj] for di in range(self.size[0]) for dj in range(self.size[0])]
                res[i][j] = max(window)

        return res



mp = MaxPooling(step=(2, 2), size=(2,2))
m1 = [[1, 10, 10], [5, 10, 0], [0, 1, 2]]
m2 = [[1, 10, 10, 12], [5, 10, 0, -5], [0, 1, 2, 300], [40, -100, 0, 54.5]]
res1 = mp(m1)
res2 = mp(m2)

assert res1 == [[10]], "неверный результат операции MaxPooling"
assert res2 == [[10, 12], [40, 300]], "неверный результат операции MaxPooling"

mp = MaxPooling(step=(3, 3), size=(2,2))
m3 = [[1, 12, 14, 12], [5, 10, 0, -5], [0, 1, 2, 300], [40, -100, 0, 54.5]]
res3 = mp(m3)
assert res3 == [[12]], "неверный результат операции при MaxPooling(step=(3, 3), size=(2,2))"

try:
    res = mp([[1, 2], [3, 4, 5]])
except ValueError:
    assert True
else:
    assert False, "некорректо отработала проверка (или она отсутствует) на не прямоугольную матрицу"

try:
    res = mp([[1, 2], [3, '4']])
except ValueError:
    assert True
else:
    assert False, "некорректо отработала проверка (или она отсутствует) на не числовые значения в матрице"
 

mp = MaxPooling(step=(1, 1), size=(5, 5))
res = mp([[5, 0, 88, 2, 7, 65],
          [1, 33, 7, 45, 0, 1],
          [54, 8, 2, 38, 22, 7],
          [73, 23, 6, 1, 15, 0],
          [4, 12, 9, 1, 76, 6],
          [0, 15, 10, 8, 11, 78]])    # [[88, 88], [76, 78]]

assert res == [[88, 88], [76, 78]], "неверный результат операции MaxPooling(step=(1, 1), size=(5, 5))"

    