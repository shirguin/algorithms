# Задание №1
# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

# Вариант 1
number = int(input('Введите трехзначное число: '))
a = number // 100
b = (number % 100) // 10
c = number % 10
summa = a + b + c
result = a * b * c
print(f"Сумма цифр числа {number}: {summa}")
print(f'Произведение цифр числа {number}: {result}')


'''
# Вариант 2
number = input('Введите трехзначное число: ')
summa = 0
result = 1
for i in number:
    summa = summa + int(i)
    result = result * int(i)
print(f"Сумма цифр числа {number}: {summa}")
print(f'Произведение цифр числа {number}: {result}')
'''
