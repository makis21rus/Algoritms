"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

import random
import timeit
import cProfile


SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
# print(array_1)

idx_min = 0
idx_max = 0
for i in range(len(array_1)):
    if array_1[i] < array_1[idx_min]:
        idx_min = i
    elif array_1[i] > array_1[idx_max]:
        idx_max = i

array_1[idx_min], array_1[idx_max] = array_1[idx_max], array_1[idx_min]
# print(array)

print(timeit.timeit('array_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]', globals=globals(), number=1000))  # 0.006323499837890267
print(timeit.timeit('array_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(20)]', globals=globals(), number=1000))  # 0.0123325998429209
print(timeit.timeit('array_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(40)]', globals=globals(), number=1000))  # 0.024434300139546394
print(timeit.timeit('array_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(80)]', globals=globals(), number=1000))  # 0.047911199973896146
print(timeit.timeit('array_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(160)]', globals=globals(), number=1000))  # 0.09666320006363094
print(timeit.timeit('array_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(320)]', globals=globals(), number=1000))  # 0.19336659996770322
print(timeit.timeit('array_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(640)]', globals=globals(), number=1000))  # 0.38428230001591146
print(timeit.timeit('array_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(1280)]', globals=globals(), number=1000))  # 0.7863680000882596
print(timeit.timeit('array_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(2560)]', globals=globals(), number=1000))  # 1.5584549000486732
print(timeit.timeit('array_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(5120)]', globals=globals(), number=1000))  # 3.0925586000084877


cProfile.run('array_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(3000)]')

#       24777 function calls in 0.007 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.001    0.001    0.007    0.007 <string>:1(<listcomp>)
#      1    0.000    0.000    0.007    0.007 <string>:1(<module>)
#   3000    0.002    0.000    0.002    0.000 random.py:239(_randbelow_with_getrandbits)
#   3000    0.003    0.000    0.005    0.000 random.py:292(randrange)
#   3000    0.001    0.000    0.006    0.000 random.py:366(randint)
#   9000    0.001    0.000    0.001    0.000 {built-in method _operator.index}
#      1    0.000    0.000    0.007    0.007 {built-in method builtins.exec}
#   3000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#   3773    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

"""Вывод: все варианты имеют линейную асимптотику, по быстродействию и эффетивности - одинаковые."""