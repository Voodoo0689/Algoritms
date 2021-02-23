
digit = int(input("введите трёхзначное число: "))

if  digit >= 100 and digit < 1000 :
    sum1 = digit % 10
    sum2 = digit % 100 // 10
    sum3 = digit // 100
    print("сумма / произведение цифр: ", sum1 + sum2 + sum3, "/", sum1 * sum2 * sum3)
else:
    print("Ошибка: число не является трёхзначным.")
