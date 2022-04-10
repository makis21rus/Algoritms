"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
import cProfile
import random
import timeit


def rep_min_max(n):
    MIN_ITEM = -100
    MAX_ITEM = 100
    array_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(n)]
    # print(array_1)

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
    return array_1


# print(rep_min_max(10))


print(timeit.timeit('rep_min_max(10)', globals=globals(), number=1000))  # 0.007313000038266182
print(timeit.timeit('rep_min_max(20)', globals=globals(), number=1000))  # 0.013879099860787392
print(timeit.timeit('rep_min_max(40)', globals=globals(), number=1000))  # 0.026734100189059973
print(timeit.timeit('rep_min_max(80)', globals=globals(), number=1000))  # 0.05229480005800724
print(timeit.timeit('rep_min_max(160)', globals=globals(), number=1000))  # 0.10413380013778806
print(timeit.timeit('rep_min_max(320)', globals=globals(), number=1000))  # 0.20912260003387928
print(timeit.timeit('rep_min_max(640)', globals=globals(), number=1000))  # 0.43154559982940555
print(timeit.timeit('rep_min_max(1280)', globals=globals(), number=1000))  # 0.8729155003093183
print(timeit.timeit('rep_min_max(2560)', globals=globals(), number=1000))  # 1.6922097001224756
print(timeit.timeit('rep_min_max(5120)', globals=globals(), number=1000))  # 3.319160799961537


cProfile.run('rep_min_max(1280)')

#       10568 function calls in 0.003 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.003    0.003 <string>:1(<module>)
#   1280    0.001    0.000    0.001    0.000 random.py:239(_randbelow_with_getrandbits)
#   1280    0.001    0.000    0.002    0.000 random.py:292(randrange)
#   1280    0.000    0.000    0.003    0.000 random.py:366(randint)
#      1    0.000    0.000    0.003    0.003 veb4_task1_var1.py:11(<listcomp>)
#      1    0.000    0.000    0.003    0.003 veb4_task1_var1.py:8(rep_min_max)
#   3840    0.000    0.000    0.000    0.000 {built-in method _operator.index}
#      1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
#   1280    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#   1601    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#      2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}

"""Вывод: все варианты имеют линейную асимптотику, первый и третий вариант одинаковы,
во втором варианте используется на один метод меньше, является более оптимальным"""
