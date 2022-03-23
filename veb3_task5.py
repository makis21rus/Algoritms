"""
5. В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и
«максимальный отрицательный». Это два абсолютно разных значения.
"""

import random

SIZE = 10
MIN_ITEM = -10
MAX_ITEM = 10
array_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array_1)

array_2 = []

for i in array_1:
    if i < 0:
        array_2.append(i)

res = array_2[0]
for j in array_2:
    if j >= res:
        res = j

print(res)
print(array_1.index(res))