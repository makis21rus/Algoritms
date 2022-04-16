"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

import random
import sys


def rep_min_max(n):
    MIN_ITEM = -100
    spam1 = sys.getsizeof(MIN_ITEM)
    MAX_ITEM = 100
    spam2 = sys.getsizeof(MAX_ITEM)
    array_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(n)]
    # print(array_1)
    spam3 = sys.getsizeof(array_1)

    idx_min = 0
    idx_max = 0
    for i in range(len(array_1)):
        if array_1[i] < array_1[idx_min]:
            idx_min = i
        elif array_1[i] > array_1[idx_max]:
            idx_max = i
    spam4 = sys.getsizeof(idx_min)
    spam5 = sys.getsizeof(idx_max)

    array_1[idx_min], array_1[idx_max] = array_1[idx_max], array_1[idx_min]

    spam_sum = spam1 + spam2 + spam3 + spam4 + spam5

    return spam_sum


print(rep_min_max(10))
# разрадность х64/х64, затрачено 296 байт памяти - наилучший вариант по затратам памяти
