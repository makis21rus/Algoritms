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

    i_max = array_1[0]
    i_min = array_1[0]

    for j in array_1:
        if j >= i_max:
            i_max = j
    for k in array_1:
        if k <= i_min:
            i_min = k
    spam4 = sys.getsizeof(i_max)
    spam5 = sys.getsizeof(i_min)
    # print(i_max)
    # print(i_min)

    a = array_1.index(i_min)
    b = array_1.index(i_max)
    # print(a, b)
    spam6 = sys.getsizeof(a)
    spam7 = sys.getsizeof(b)

    array_1[a] = i_max
    array_1[b] = i_min

    spam_sum = spam1 + spam2 + spam3 + spam4 + spam5 + spam6 + spam7
    return spam_sum


print(rep_min_max(10))
# разрадность х64/х64, затрачено 352 байта памяти
