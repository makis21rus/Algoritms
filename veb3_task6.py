"""
6. В одномерном массиве найти сумму элементов, находящихся между
минимальным и максимальным элементами. Сами минимальный и
максимальный элементы в сумму не включать
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

a = array_1.index(i_min)
b = array_1.index(i_max)
res = 0

print(i_max)
print(i_min)
if a < b:
    for l in array_1[a+1:b]:
        res += l
else:
    for l in array_1[b+1:a]:
        res += l
print(res)
