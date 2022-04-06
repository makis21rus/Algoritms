"""
Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход
натуральное и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.
"""
import cProfile
import timeit


def search_prime(n):
    count = 0
    number = 1
    prime = [2]
    if n == 0:
        return 2
    while count != n:
        number += 2

        for num in prime:
            if number % num == 0:
                break
        else:
            count += 1
            prime.append(number)
    return number


print(timeit.timeit('search_prime(10)', globals=globals(), number=1000))  # 0.003757599974051118
print(timeit.timeit('search_prime(20)', globals=globals(), number=1000))  # 0.011532100150361657
print(timeit.timeit('search_prime(40)', globals=globals(), number=1000))  # 0.03910819999873638
print(timeit.timeit('search_prime(80)', globals=globals(), number=1000))  # 0.13577229995280504
print(timeit.timeit('search_prime(160)', globals=globals(), number=1000))  # 0.4928201998118311
print(timeit.timeit('search_prime(320)', globals=globals(), number=1000))  # 1.94964970019646
print(timeit.timeit('search_prime(640)', globals=globals(), number=1000))  # 7.955392100149766
print(timeit.timeit('search_prime(1280)', globals=globals(), number=1000))  # 32.313576200045645


cProfile.run('search_prime(160)')
#       164 function calls in 0.003 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.003    0.003 <string>:1(<module>)
#      1    0.003    0.003    0.003    0.003 veb4_task2_ver2.py:11(search_prime)
#      1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
#    160    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""Вывод: 1-й вариант более быстродействующий и эффективный, имеет константную асимптотику.
второй вариант - медленнее, асимптотика квадратичная"""
