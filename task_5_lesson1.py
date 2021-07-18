# Задание №5
# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько
# между ними находится букв.

letter_1 = str.upper(input('Введите первую букву: '))
letter_2 = str.upper(input('Введите вторую букву: '))

code_letter_1 = ord(letter_1.encode('cp1251'))
code_letter_2 = ord(letter_2.encode('cp1251'))

if 65 <= code_letter_1 <= 90 and 65 <= code_letter_2 <= 90:
    print(f'Буква {letter_1} находится на {code_letter_1 - 64} месте английского алфавита')
    print(f'Буква {letter_2} находится на {code_letter_2 - 64} месте ангглийского алфавита')
    print(f'Между буквой {letter_1} и буквой {letter_2} находится еще {abs((code_letter_2-64)-(code_letter_1-64))-1} буквы')
elif 192 <= code_letter_1 <= 223 and 192 <= code_letter_2 <= 223:
    print(f'Буква {letter_1} находится на {code_letter_1 - 191} месте русского алфавита')
    print(f'Буква {letter_2} находится на {code_letter_2 - 191} месте русского алфавита')
    print(f'Между буквой {letter_1} и буквой {letter_2} находится еще {abs((code_letter_2 - 191) - (code_letter_1 - 191)) - 1} буквы')
else:
    print('Один или оба символа не являются буквами английского или русского алфавитов')
print()
print('Работа программы завершена')
# в программе не учтена буква Ё русского алфавита
