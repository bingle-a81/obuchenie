import numpy as np
# Создаем массив целых чисел
arr = np.array(input(),dtype=None)
print(arr)
# Преобразуем его в массив с плавающей точкой
arr_float = arr.astype(float)
print(arr_float) # out: [1. 2. 3. 4. 5.]