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

min_num = min(array_1)
max_num = max(array_1)
idx_min = array_1.index(min_num)
idx_max = array_1.index(max_num)
array_1[idx_min], array_1[idx_max] = array_1[idx_max], array_1[idx_min]
# print(array)

print(timeit.timeit('array_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]', globals=globals(), number=1000))  # 0.006289100041612983
print(timeit.timeit('array_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(20)]', globals=globals(), number=1000))  # 0.012129100039601326
print(timeit.timeit('array_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(40)]', globals=globals(), number=1000))  # 0.02389850001782179
print(timeit.timeit('array_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(80)]', globals=globals(), number=1000))  # 0.047640400007367134
print(timeit.timeit('array_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(160)]', globals=globals(), number=1000))  # 0.09641720005311072
print(timeit.timeit('array_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(320)]', globals=globals(), number=1000))  # 0.18922140006907284
print(timeit.timeit('array_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(640)]', globals=globals(), number=1000))  # 0.38323520007543266
print(timeit.timeit('array_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(1280)]', globals=globals(), number=1000))  # 0.7923181001096964
print(timeit.timeit('array_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(2560)]', globals=globals(), number=1000))  # 1.5521404000464827
print(timeit.timeit('array_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(5120)]', globals=globals(), number=1000))  # 3.0912576999980956


cProfile.run('array_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(3000)]')

#       24770 function calls in 0.007 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.001    0.001    0.007    0.007 <string>:1(<listcomp>)
#     1    0.000    0.000    0.007    0.007 <string>:1(<module>)
#  3000    0.001    0.000    0.002    0.000 random.py:239(_randbelow_with_getrandbits)
#  3000    0.003    0.000    0.005    0.000 random.py:292(randrange)
#  3000    0.001    0.000    0.006    0.000 random.py:366(randint)
#  9000    0.001    0.000    0.001    0.000 {built-in method _operator.index}
#     1    0.000    0.000    0.007    0.007 {built-in method builtins.exec}
#  3000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#  3766    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

"""Вывод: все варианты имеют линейную асимптотику, по быстродействию и эффетивности - одинаковые."""
