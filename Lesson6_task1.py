"""
Python 3.9.1
Windows 10 x64
На примере числа: 789987789987
"""
import sys

def summary(*args):
    variables_nam = [*args]
    forsumm = []
    for j in variables_nam:
        forsumm.append(sys.getsizeof(j))
        print(sys.getsizeof(j))
    return(sum(forsumm))

num = 789987789987

even, odd = 0, 0
while num > 0:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
    num = num // 10
print(f"четных - {even}, нечетных - {odd}")


print(summary(num, even, odd))

    # num 24 байт, even 28 байт, odd 28 байт
    #сумма 80 байт


num = str(num)
even = odd = 0
for i in num:
    if i in {'0', '2', '4', '6', '8'}:
        even += 1
    else:
        odd += 1
print(f"четных - {even}, нечетных - {odd}")


print(summary(num, even, odd, i))
    # num 50 байт
    # even 28 байт, odd 28 байт, переменная i 50 байт
    # Требуется больше памяти из-за дополнительной переменной.
    # сумма 152

def even_odd(number, even_=0, odd_=0):
    if number == 0:
        return even_, odd_
    if number % 2 == 0:
        even_ += 1
    else:
        odd_ += 1
    number = number // 10
    return even_odd(number, even_, odd_)
num = 789987789987
print(even_odd(num))


def show(obj):
    print(f'{type(obj)=}, {sys.getsizeof(obj)=}, {obj}')
show(even_odd)
# type(obj)=<class 'function'>, sys.getsizeof(obj)=136, <function even_odd at 0x000001F671EEE040>
# размер самой функции, как объекта в памяти
show(even_odd(num))
# type(obj)=<class 'tuple'>, sys.getsizeof(obj)=56, (4, 8) 56 байт - размер результата фунуции.





