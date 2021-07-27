# Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования Решета Эратосфена;
# Использовать алгоритм решето Эратосфена

import timeit
import cProfile

def not_eratosthenes(n):
    """ n - число до которого нужно вывести список простых чисел"""
    a = []
    for i in range(2, n):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            a.append(i)
    return a


def eratosthenes(n):
    """ n - число до которого нужно вывести список простых чисел"""
    a = [0] * n
    for i in range(n):
        a[i] = i
    a[1] = 0
    m = 2
    while m < n:
        if a[m] != 0:
            j = m * 2
            while j < n:
                a[j] = 0
                j = j + m
        m += 1
    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])
    return b


"""Проверяем работу функций"""
# print(not_eratosthenes(1000))
# print(eratosthenes(1000))

"""Оцениваем по времени"""
print(f'not_eratosthenes - {timeit.timeit(stmt="not_eratosthenes(500)", setup="from __main__ import not_eratosthenes", number=1000)}')
print(f'eratosthenes     - {timeit.timeit(stmt="eratosthenes(500)", setup="from __main__ import eratosthenes", number=1000)}')
print(f'Решето Эратосфера работает в {(timeit.timeit(stmt="not_eratosthenes(500)", setup="from __main__ import not_eratosthenes", number=1000)) / (timeit.timeit(stmt="eratosthenes(500)", setup="from __main__ import eratosthenes", number=1000))} раз быстрее')

"""Анализируем через Profile"""
# cProfile.run('not_eratosthenes(1000)')
# cProfile.run('eratosthenes(1000)')

# По моему мнению причина медленной работы not_eratosthenes в операции вычисления дробной части при целочисленном делении.
