# Задание №1
# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из
# чисел в диапазоне от 2 до 9.

i = 2
list_result = []
while i <= 9:
    count = 0
    n = 2
    list_temp = []
    while n <= 99:
        if n % i == 0:
            count += 1
        n += 1
    list_temp = [i, count]
    list_result.append(list_temp)
    i += 1
print('Кратность чисел от 2 до 9 в диапазоне чисел от 2 до 99:')
el = 0
while el < len(list_result):
    print(f'числу {list_result[el][0]} кратно {list_result[el][1]} чисел')
    el += 1
print(f'\nПрограмма завершена.')
