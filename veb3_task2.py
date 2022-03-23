"""
2. Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй
массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля),
т.к. именно в этих позициях первого массива стоят четные числа.
"""
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 10
array_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array_1)

array_2 = []

for i in array_1:
    if i % 2 == 0:
        res = array_1.index(i)
        array_1[res] = 1   # хитрый ход
        array_2.append(res)
print(array_2)
