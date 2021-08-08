# Задание №1
# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный
# случайными числами на промежутке [-100; 100). Выведите на экран исходный и
# отсортированный массивы. Сортировка должна быть реализована в виде функции. По
# возможности доработайте алгоритм (сделайте его умнее).

import random


def sort_bubble(ls):
    result_ls = ls
    n = 1
    while n < len(result_ls):
        for i in range(len(result_ls) - n):
            if result_ls[i] < result_ls[i + 1]:
                result_ls[i], result_ls[i + 1] = result_ls[i + 1], result_ls[i]
        n += 1
    return result_ls


len_ls_data = int(input('Введите длину массива: '))
ls_data = [random.randint(-100, 100) for i in range(len_ls_data)]
print(f'Массив:                 {ls_data}')
print(f'Отсортированный массив: {sort_bubble(ls_data)}')
