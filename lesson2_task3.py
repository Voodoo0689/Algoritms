def rec(x):
    text = ''.join(reversed(x))
    return text


print("Введите натуральное число")
numbers = input("Ваше число?: ")
print(rec(numbers))

