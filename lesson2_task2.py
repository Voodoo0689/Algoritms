print("Введите натуральное число")
num = input("Ваше число?: ")
even = 0
not_even = 0
for i in num:
    if int(i) % 2 == 0:
        even += 1
    else:
        not_even += 1
print(even, not_even)
