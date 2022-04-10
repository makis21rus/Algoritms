"""
Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел.
При этом каждое число представляется как коллекция, элементы которой — цифры числа. Например,
пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’]
соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение -
[‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

from collections import deque


numbers = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12,
           'D': 13, 'E': 14, 'F': 15}
numbers_reverse = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': "A", '11': "B",
                   '12': "C", '13': "D", '14': "E", '15': "F"}

number_a = deque(input('Введите первое число в шестнадцатиричном формате: ').upper())
number_b = deque(input('Введите второе число в шестнадцатиричном формате: ').upper())

print(number_a, number_b, sep='\n')

for i in range(len(number_a)):
    number_a[i] = numbers[number_a[i]]
for i in range(len(number_b)):
    number_b[i] = numbers[number_b[i]]

# print(number_a, number_b, sep='\n')

while len(number_a) != len(number_b):
    if len(number_a) > len(number_b):
        number_b.appendleft(0)
    else:
        number_a.appendleft(0)

number_b.appendleft(0)
number_a.appendleft(0)

# print(number_a, number_b, sep='\n')

j = len(number_a)
num_sum = deque()

while j > 0:
    d = number_a[j-1] + number_b[j-1]
    if d >= 16:
        number_a[j - 2] += 1
        d = d - 16
    num_sum.appendleft(d)
    j -= 1

if num_sum[0] == 0:
    del num_sum[0]

# print(num_sum)
for i in range(len(num_sum)):
    num_sum[i] = str(num_sum[i])
    num_sum[i] = numbers_reverse[num_sum[i]]

print(f'Результат сложения в шестнадцатиричном формате: {num_sum}')
