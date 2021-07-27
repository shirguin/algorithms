# Проанализировать скорость и сложность одного любого алгоритма, разработанных в
# рамках практического задания первых трех уроков.

import random
import timeit
import cProfile

"""Формируем матрицу"""
def matrix_creation(a, b):
    # a - количество столбцов матрицы
    # b - количество строк матрицы
    list_data = []
    i = b
    while i > 0:
        ls = []
        i1 = a
        while i1 > 0:
            ls.append(random.randint(1, 100))
            i1 -= 1
        list_data.append(ls)
        i -= 1
    return list_data


"""Заменяем цикл формирования строки матрицы на генератор"""
def matrix_creation_1(a, b):
    # a - количество столбцов матрицы
    # b - количество строк матрицы
    list_data = []
    i = b
    while i > 0:
        ls = [random.randint(1, 100) for i in range(a)]
        list_data.append(ls)
        i -= 1
    return list_data


"""Отказываемся от использования дополнительной переменной"""
def matrix_creation_2(a, b):
    # a - количество столбцов матрицы
    # b - количество строк матрицы
    list_data = []
    while b > 0:
        ls = [random.randint(1, 100) for i in range(a)]
        list_data.append(ls)
        b -= 1
    return list_data


"""формируем матрицу с помощью генератора, вложенного в генератор"""
def matrix_creation_3(a, b):
    # a - количество столбцов матрицы
    # b - количество строк матрицы
    list_data = [[random.randint(1, 100) for i in range(a)] for j in range(b)]
    return list_data


"""Проверяем работу каждой функции"""
# print(matrix_creation(20, 20))
# print(matrix_creation_1(20, 20))
# print(matrix_creation_2(20, 20))
# print(matrix_creation_3(20, 20))

"""Оцениваем по времени"""
print(f'matrix_creation    - {timeit.timeit(stmt="matrix_creation(20, 20)", setup="from __main__ import matrix_creation", number=1000)}')
print(f'matrix_creation_1  - {timeit.timeit(stmt="matrix_creation_1(20, 20)", setup="from __main__ import matrix_creation_1", number=1000)}')
print(f'matrix_creation_2  - {timeit.timeit(stmt="matrix_creation_2(20, 20)", setup="from __main__ import matrix_creation_2", number=1000)}')
print(f'matrix_creation_3  - {timeit.timeit(stmt="matrix_creation_3(20, 20)", setup="from __main__ import matrix_creation_3", number=1000)}')
"""В большинстве случаев 4 вариант работает быстрее. Плюс самый короткий код"""

"""Анализируем через Profile"""
# cProfile.run('matrix_creation(20, 20)')
# cProfile.run('matrix_creation_1(20, 20)')
# cProfile.run('matrix_creation_2(20, 20)')
# cProfile.run('matrix_creation_3(20, 20)')
