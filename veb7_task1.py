"""
1) Отсортируйте по убыванию методом пузырька одномерный целочисленный
массив, заданный случайными числами на промежутке [-100; 100).
Выведите на экран исходный и отсортированный массивы.
"""

import random


def my_sort(array):
    while array != sorted(array, reverse=True):
        for i in range(len(array) - 1):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
    return array


array_1 = [random.randrange(-100, 100) for _ in range(10)]
print(f'Изначальный массив - {array_1}')
print(f'Отсортированный массив - {my_sort(array_1)}')
