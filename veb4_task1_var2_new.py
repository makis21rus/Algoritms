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

    idx_min = 0
    idx_max = 0
    for i in range(len(array_1)):
        if array_1[i] < array_1[idx_min]:
            idx_min = i
        elif array_1[i] > array_1[idx_max]:
            idx_max = i

    array_1[idx_min], array_1[idx_max] = array_1[idx_max], array_1[idx_min]
    return array_1
    # print(array)


print(timeit.timeit('rep_min_max(10)', globals=globals(), number=1000))  # 0.007384800352156162
print(timeit.timeit('rep_min_max(20)', globals=globals(), number=1000))  # 0.013742499984800816
print(timeit.timeit('rep_min_max(40)', globals=globals(), number=1000))  # 0.026627799961715937
print(timeit.timeit('rep_min_max(80)', globals=globals(), number=1000))  # 0.05521759996190667
print(timeit.timeit('rep_min_max(160)', globals=globals(), number=1000))  # 0.11000100011005998
print(timeit.timeit('rep_min_max(320)', globals=globals(), number=1000))  # 0.21525749983265996
print(timeit.timeit('rep_min_max(640)', globals=globals(), number=1000))  # 0.45063679991289973
print(timeit.timeit('rep_min_max(1280)', globals=globals(), number=1000))  # 0.8815205995924771
print(timeit.timeit('rep_min_max(2560)', globals=globals(), number=1000))  # 1.7356805996969342
print(timeit.timeit('rep_min_max(5120)', globals=globals(), number=1000))  # 3.430985199753195


cProfile.run('rep_min_max(1280)')

#       10601 function calls in 0.003 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.003    0.003 <string>:1(<module>)
#   1280    0.001    0.000    0.001    0.000 random.py:239(_randbelow_with_getrandbits)
#   1280    0.001    0.000    0.002    0.000 random.py:292(randrange)
#   1280    0.000    0.000    0.003    0.000 random.py:366(randint)
#      1    0.000    0.000    0.003    0.003 veb4_task1_var2.py:10(rep_min_max)
#      1    0.000    0.000    0.003    0.003 veb4_task1_var2.py:13(<listcomp>)
#   3840    0.000    0.000    0.000    0.000 {built-in method _operator.index}
#      1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#   1280    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#   1635    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


"""Вывод: все варианты имеют линейную асимптотику, первый и третий вариант одинаковы,
во втором варианте используется на один метод меньше, является более оптимальным"""
