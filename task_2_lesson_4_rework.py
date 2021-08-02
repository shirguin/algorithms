# Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования Решета Эратосфена;
# Использовать алгоритм решето Эратосфена
import math
import timeit
import cProfile

def not_eratosthenes(n):
    """ n - порядковый номер простого числа"""
    a = [2]
    count = 1
    number = 3
    while count < n:
        flag = True
        for i in a:
            if number % i == 0:
                flag = False
                break
        if flag:
            count += 1
            a.append(number)
        number += 1
    return a[-1]


def prime_counting_function(n):
    '''Функция вычисляет количество елементов в списке, содержащим "n" простых чисел'''
    # Функция выдает длину списка больше, чем это надо. Возможно эти элементы нужны для вычисления последнего простого числа.
    # Ниже пример отработки функции со значением n = 10. С увеличением значения "n", количество лишних элементов растет
    # [0, 0, 2, 3, 0, 5, 0, 7, 0, 0, 0, 11, 0, 13, 0, 0, 0, 17, 0, 19, 0, 0, 0, 23, 0, 0, 0, 0, 0, 29, 0, 31, 0, 0, 0, 0, 0]
    # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    count_of_primes = 0
    cur_number = n
    while count_of_primes <= n:
        count_of_primes = cur_number / math.log(cur_number)
        cur_number += 1
    return cur_number


def eratosthenes(n):
    """ n - порядковый номер простого числа"""
    # Вариант показанный на уроке работает не совсем верно:
    # теряются некоторые простые числа или я что то не допонял.
    # Ниже пример отработки функции со значением n = 20
    # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
    # [2, 3, 7, 13, 19, 25, 31, 39, 43, 49, 55, 61, 69, 73, 81, 85]

    # n_max = prime_counting_function(n)
    # a = [_ for _ in range(2, n_max)]
    # len_a = len(a)
    #
    # for number in a:
    #     if number != 0:
    #         for j in range(number, len_a, number):
    #             a[j] = 0
    #
    # b = [i for i in a if i != 0]
    # print(b)
    # return b[-1]

    # Алгоритм моего варианта не очень хорош, так как много повторений, но другого придумать не смог.
    a = []
    count = 1
    num_el = n
    while count < n:
        a = [x for x in range(0, num_el)]
        a[1] = 0
        count = 0
        m = 2
        while m <= num_el-1:
            if a[m] != 0:
                count += 1
                j = m * 2
                while j < num_el:
                    a[j] = 0
                    j = j + m
            m += 1
        num_el += 1
    b = [x for x in a if x != 0]
    return b[-1]


'''Вариант с использованием функции prime_counting_function'''
def eratosthenes_1(n):
    num_el = prime_counting_function(n)
    a = [x for x in range(0, num_el)]
    a[1] = 0
    count = 0
    m = 2
    while m <= num_el - 1:
        if a[m] != 0:
            count += 1
            j = m * 2
            while j < num_el:
                a[j] = 0
                j = j + m
        m += 1
    b = [x for x in a if x != 0]
    return b[-1]


i = int(input('Введите номер по счету простого числа: '))

"""Проверяем работу функций"""
print(f'Метод not_eratosthenes - под номером {i} находится число: {not_eratosthenes(i)}')
print(f'Метод eratosthenes     - под номером {i} находится число: {eratosthenes(i)}')
print(f'Метод eratosthenes_1   - под номером {i} находится число: {eratosthenes(i)}')

"""Оцениваем по времени"""
print(f'not_eratosthenes - {timeit.timeit(stmt="not_eratosthenes(20)", setup="from __main__ import not_eratosthenes", number=50)}')
print(f'eratosthenes     - {timeit.timeit(stmt="eratosthenes(20)", setup="from __main__ import eratosthenes", number=50)}')
print(f'eratosthenes_1   - {timeit.timeit(stmt="eratosthenes_1(20)", setup="from __main__ import eratosthenes_1", number=50)}')

"""Анализируем через Profile"""
# cProfile.run('not_eratosthenes(1000)')
# cProfile.run('eratosthenes(1000)')
# cProfile.run('eratosthenes_1(1000)')

# Получилось так, что мой алгоритм с использованием решета Эротосфена работает медленнее
# not_eratosthenes - 0.003019922000000008
# eratosthenes     - 0.055526803000000235
# eratosthenes_1   - 0.0035775710000001126
