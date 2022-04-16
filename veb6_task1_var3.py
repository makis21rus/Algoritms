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
    spam3 = sys.getsizeof(array_1)
    # print(array_1)

    min_num = min(array_1)
    spam4 = sys.getsizeof(min_num)
    max_num = max(array_1)
    spam5 = sys.getsizeof(max_num)
    idx_min = array_1.index(min_num)
    spam6 = sys.getsizeof(idx_min)
    idx_max = array_1.index(max_num)
    spam7 = sys.getsizeof(idx_max)
    array_1[idx_min], array_1[idx_max] = array_1[idx_max], array_1[idx_min]
    spam_sum = spam1 + spam2 + spam3 + spam4 + spam5 + spam6 + spam7
    return spam_sum


print(rep_min_max(10))
# разрадность х64/х64, затрачено 352 байта памяти
