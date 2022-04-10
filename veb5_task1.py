"""Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для
каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести
наименования предприятий, чья прибыль выше среднего и ниже среднего."""

import collections


comp_count = int(input('Введите количество предприятий: '))

companies = collections.defaultdict()
profit_companies = collections.deque()
unprofit_companies = collections.deque()
common_profit = 0

for i in range(comp_count):
    comp_name = input(f'Введите название {i+1}-го предприятия: ')
    profit = 0
    j = 1
    while j <= 4:
        profit_kv = float(input(f'Введите прибыль за {j}-й квартал: '))
        j += 1
        profit = profit + profit_kv
    companies[comp_name] = profit
    common_profit = common_profit + profit

mid_profit = common_profit / comp_count
for i, item in companies.items():
    if item >= mid_profit:
        profit_companies.append(i)
    else:
        unprofit_companies.append(i)
print(f'Средняя прибыль для всех компаний: {mid_profit}')
print(f'Прибыль выше среднего у следующих компаний:')
for name in profit_companies:
    print(name)
print(f'Прибыль ниже среднего у следующих компаний:')
for name in unprofit_companies:
    print(name)
