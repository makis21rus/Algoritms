"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

import random
import timeit
import cProfile


def rep_min_max(n):
    MIN_ITEM = -100
    MAX_ITEM = 100
    array_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(n)]
    # print(array_1)

    min_num = min(array_1)
    max_num = max(array_1)
    idx_min = array_1.index(min_num)
    idx_max = array_1.index(max_num)
    array_1[idx_min], array_1[idx_max] = array_1[idx_max], array_1[idx_min]
    return array_1
    # print(array)


print(timeit.timeit('rep_min_max(10)', globals=globals(), number=1000))  # 0.007245799992233515
print(timeit.timeit('rep_min_max(20)', globals=globals(), number=1000))  # 0.013702599797397852
print(timeit.timeit('rep_min_max(40)', globals=globals(), number=1000))  # 0.026080600451678038
print(timeit.timeit('rep_min_max(80)', globals=globals(), number=1000))  # 0.050939599983394146
print(timeit.timeit('rep_min_max(160)', globals=globals(), number=1000))  # 0.10737639991566539
print(timeit.timeit('rep_min_max(320)', globals=globals(), number=1000))  # 0.22603419981896877
print(timeit.timeit('rep_min_max(640)', globals=globals(), number=1000))  # 0.4102185000665486
print(timeit.timeit('rep_min_max(1280)', globals=globals(), number=1000))  # 0.8095559002831578
print(timeit.timeit('rep_min_max(2560)', globals=globals(), number=1000))  # 1.6087026996538043
print(timeit.timeit('rep_min_max(5120)', globals=globals(), number=1000))  # 3.1553702000528574


cProfile.run('rep_min_max(1280)')

#       10582 function calls in 0.003 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.003    0.003 <string>:1(<module>)
#   1280    0.001    0.000    0.001    0.000 random.py:239(_randbelow_with_getrandbits)
#   1280    0.001    0.000    0.002    0.000 random.py:292(randrange)
#   1280    0.000    0.000    0.003    0.000 random.py:366(randint)
#      1    0.000    0.000    0.003    0.003 veb4_task1_var3.py:10(rep_min_max)
#      1    0.000    0.000    0.003    0.003 veb4_task1_var3.py:13(<listcomp>)
#   3840    0.000    0.000    0.000    0.000 {built-in method _operator.index}
#      1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.min}
#   1280    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#   1613    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#      2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}

"""Вывод: все варианты имеют линейную асимптотику, первый и третий вариант одинаковы,
во втором варианте используется на один метод меньше, является более оптимальным"""
