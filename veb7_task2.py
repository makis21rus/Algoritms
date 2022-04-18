"""
2). Отсортируйте по возрастанию методом слияния одномерный
вещественный массив, заданный случайными числами на промежутке
[0; 50). Выведите на экран исходный и отсортированный массивы.
"""

import random


def merge_sort(array):

    if len(array) <= 1:
        return array
    left_array = merge_sort(array[:len(array) // 2])
    right_array = merge_sort(array[len(array) // 2:])
    i = j = 0
    res = []

    while i < len(left_array) or j < len(right_array):
        if i >= len(left_array):
            res.append(right_array[j])
            j += 1
        elif j >= len(right_array):
            res.append(left_array[i])
            i += 1
        elif left_array[i] < right_array[j]:
            res.append(left_array[i])
            i += 1
        else:
            res.append(right_array[j])
            j += 1
        # print(res)
    return res


array_1 = [round(random.uniform(0, 50), 1) for i in range(10)]
print(f'Изначальный массив - {array_1}')
print(f'Отсортированный массив - {merge_sort(array_1)}')
