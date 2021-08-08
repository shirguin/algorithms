# Задание №2
# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный
# случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный
# массивы.

import random


'''Функция разделения массива'''


def merge_sort(ls):
    if len(ls) <= 1:
        return ls
    mid = len(ls) // 2
    left, right = merge_sort(ls[:mid]), merge_sort(ls[mid:])

    return merge(left, right, ls.copy())


'''Функция сортировки массива методом слияния'''


def merge(left, right, ls):
    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):
        if left[left_cursor] <= right[right_cursor]:
            ls[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            ls[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1

    for left_cursor in range(left_cursor, len(left)):
        ls[left_cursor + right_cursor] = left[left_cursor]

    for right_cursor in range(right_cursor, len(right)):
        ls[left_cursor + right_cursor] = right[right_cursor]

    return ls


len_ls_data = int(input('Введите длину массива: '))
ls_data = [round(random.uniform(0, 50), 2) for i in range(len_ls_data)]
print(f'Массив:                 {ls_data}')
print(f'Отсортированный массив: {merge_sort(ls_data)}')
