# Задание №9
# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

def sum_number(number):
    sum_numb = 0
    for i in number:
        sum_numb += int(i)
    return sum_numb


list_number = [i for i in input('Введите натуральные числа через пробел: ').split()]

max_number = 0
max_sum_number = 0
for el in list_number:
    if sum_number(el) > max_sum_number:
        max_number = el
        max_sum_number = sum_number(el)

print(f'Среди натуральных чисел {list_number}\nбольшим по сумме цифр, являерся число {max_number}, сумма цифр - {max_sum_number}\n')
print('Программа завершена.')

# Мы не знаем сколько чисел пользователь будет вводить, поэтому пришлось использовать список.
