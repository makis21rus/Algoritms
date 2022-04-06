"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
import cProfile
import random
import timeit

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
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
# print(array_1)


print(timeit.timeit('array_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]', globals=globals(), number=1000))  # 0.0064356999937444925
print(timeit.timeit('array_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(20)]', globals=globals(), number=1000))  # 0.012385499896481633
print(timeit.timeit('array_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(40)]', globals=globals(), number=1000))  # 0.024347800062969327
print(timeit.timeit('array_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(80)]', globals=globals(), number=1000))  # 0.0480430000461638
print(timeit.timeit('array_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(160)]', globals=globals(), number=1000))  # 0.0962679001968354
print(timeit.timeit('array_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(320)]', globals=globals(), number=1000))  # 0.18979159998707473
print(timeit.timeit('array_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(640)]', globals=globals(), number=1000))  # 0.39105989993549883
print(timeit.timeit('array_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(1280)]', globals=globals(), number=1000))  # 0.781145199900493
print(timeit.timeit('array_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(2560)]', globals=globals(), number=1000))  # 1.553919400088489
print(timeit.timeit('array_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(5120)]', globals=globals(), number=1000))  # 3.090824899962172


cProfile.run('array_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(3000)]')

#       24871 function calls in 0.007 seconds
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
#   3867    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

"""Вывод: все варианты имеют линейную асимптотику, по быстродействию и эффетивности - одинаковые."""
