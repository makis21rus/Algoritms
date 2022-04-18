
import random

m = int(input('Введите натуральное число: '))
array_1 = [(random.randint(0, 5)) for i in range(2 * m + 1)]
print(f'Исходный массив: \n{array_1}')


less = []
more = []
pivots = []
mid = ''
n = 0
while mid == '':
    pivot = array_1[n]
    for item in array_1:
        if item < pivot:
            less.append(item)
        elif item > pivot:
            more.append(item)
        else:
            pivots.append(item)

    while len(pivots) > 1:
        if len(less) > len(more):
            more.append(pivots.pop())
        elif len(less) < len(more):
            less.append(pivots.pop())
        else:
            more.append(pivots.pop())

    if len(less) == len(more):
        mid = pivots[0]
    else:
        n += 1
        less = []
        more = []
        pivots = []


print(f'Медианой является число {mid}')

print(f'Отсортированный массив, чтобы убедиться в этом: \n{sorted(array_1)}')  # для проверки
