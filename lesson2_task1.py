def math(operation, x, y):
    if operation == "+":
        return x + y
    elif operation == "-":
        return x - y
    elif operation == "*":
        return x * y
    elif operation == "/":
        return x / y
    else: print("Поддерживаются только /, * , -, + операции")

while True:
    sign = input('Что будем делать? Введите "/, *, -, +" ?: ')
    if sign == "0":
        break
    first_number = int(input("Ведите первое натуральное число: "))
    second_number = int(input("Ведите второе натуральное число: "))
    print(math(sign, first_number, second_number))

