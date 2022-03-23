"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array_1)

i_max = array_1[0]
i_min = array_1[0]

for j in array_1:
    if j >= i_max:
        i_max = j
for k in array_1:
    if k <= i_min:
        i_min = k

# print(i_max)
# print(i_min)

a = array_1.index(i_min)
b = array_1.index(i_max)
# print(a, b)

array_1[a] = i_max
array_1[b] = i_min
print(array_1)
