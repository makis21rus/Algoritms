"""
Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход
натуральное и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.
"""
import cProfile
import timeit

n = 100000


sieve = [i for i in range(n)]
HOLE = 0
sieve[1] = HOLE

for i in range(2, n):
    if sieve[i] != HOLE:
        j = i + i
        while j < n:
            sieve[j] = HOLE
            j += i

# print(sieve)
res = [item for item in sieve if item != HOLE]
# print(res)
num = res[10]
# print(num)


print(timeit.timeit('num = res[10]', globals=globals(), number=1000))  # 2.7700094506144524e-05
print(timeit.timeit('num = res[20]', globals=globals(), number=1000))  # 2.7900096029043198e-05
print(timeit.timeit('num = res[40]', globals=globals(), number=1000))  # 2.9399991035461426e-05
print(timeit.timeit('num = res[80]', globals=globals(), number=1000))  # 2.7799978852272034e-05
print(timeit.timeit('num = res[160]', globals=globals(), number=1000))  # 3.0800001695752144e-05
print(timeit.timeit('num = res[320]', globals=globals(), number=1000))  # 2.9900111258029938e-05
print(timeit.timeit('num = res[640]', globals=globals(), number=1000))  # 2.7300091460347176e-05
print(timeit.timeit('num = res[1280]', globals=globals(), number=1000))  # 2.750009298324585e-05

cProfile.run('num = res[160]')

#       3 function calls in 0.000 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


"""Вывод: 1-й вариант более быстродействующий и эффективный, имеет константную асимптотику"""
