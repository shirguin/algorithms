# Задание №1
# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4
# квартала (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить
# среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий, чья
# прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже
# среднего.

import collections

Company = collections.namedtuple('Company', ['quarter1', 'quarter2', 'quarter3', 'quarter4'])
enterprises = {}

n = int(input("Введите количество предприятий: "))

for i in range(n):
    name_company = input(f'Введите название {i+1} предприятия: ')
    enterprises[name_company] = Company(
        quarter1=float(input('Введите прибыль за 1-й квартал: ')),
        quarter2=float(input('Введите прибыль за 2-й квартал: ')),
        quarter3=float(input('Введите прибыль за 3-й квартал: ')),
        quarter4=float(input('Введите прибыль за 4-й квартал: '))
    )
# print(enterprises)

total_profit = 0
for name_company, profit in enterprises.items():
    total_profit += sum(profit)

avg_total_profit = total_profit / len(enterprises)
print(f'Средняя годовая прибыль для всех предприятий: {round(avg_total_profit, 2)}\n')

print('Предприятия с прибылью выше средней: ')
for name_company, profit in enterprises.items():
    if sum(profit) > avg_total_profit:
        print(f'{name_company} ({round(sum(profit), 2)})')
print()
print('Предприятия с прибылью ниже средней: ')
for name_company, profit in enterprises.items():
    if sum(profit) < avg_total_profit:
        print(f'{name_company} ({round(sum(profit), 2)})')
