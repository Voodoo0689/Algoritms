seq = input('Введите последовательность из натуральных чисел: ')
search = input('Введите цифру для поиска: ')
count = 0

for i in seq:
    if i == search:
        count += 1

print(
    f'Цифра встречается {search} в последовательности {seq}: \
{count} раз(а)'
        )
