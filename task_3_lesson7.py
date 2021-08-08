# Задание №3
# Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите
# в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части: в
# одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
# Задачу можно решить без сортировки исходного массива. Но если это слишком сложно, то
# используйте метод сортировки, который не рассматривался на уроках.

import random


def finding_median(ls_data):
    median = 0
    for i in range(0, len(ls_data)):
        min_count = 0
        max_count = 0
        for j in range(0, len(ls_data)):
            if ls_data[i] > ls_data[j]:
                min_count += 1
            elif ls_data[i] < ls_data[j]:
                max_count += 1
        if min_count == max_count:
            median = ls_data[i]
            break
    return median


m = int(input('Введите значение "m": '))
min_value = int(input('Введите минимальное значение элемента массива : '))
max_value = int(input('Введите максимальное значение элемента массива: '))
size = 2 * m + 1
list_data = [random.randint(min_value, max_value) for i in range(size)]

med = finding_median(list_data)
left_ls = sorted([el for el in list_data if el < med])
right_ls = sorted([el for el in list_data if el > med])

print(f'Массив:               {list_data}')
print(f'Значение медианы: {med}  {left_ls} [{finding_median(list_data)}] {right_ls}')
