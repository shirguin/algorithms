# Задание №8
# Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. Программа
# должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю
# ячейку строки. В конце следует вывести полученную матрицу.

list_data = []
i = 1
while i <= 4:
    ls = []
    el = 1
    while el <= 4:
        ls.append(int(input(f'Введите значение {el} столбца {i} строки: ')))
        el += 1
    sum_ls = sum(ls)
    ls.append(sum_ls)
    list_data.append(ls)
    i += 1
el1 = 0
while el1 < len(list_data):
    el2 = 0
    while el2 < len(list_data[el1]):
        print(f'{list_data[el1][el2]:3}', end='   ')
        el2 += 1
    print()
    el1 += 1

print('Программа завершена.')
