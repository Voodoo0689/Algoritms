'''
1). Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
Примечания:
● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
  Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.
'''

from random import randint
from timeit import timeit

max_size = 10
number_execution = 10_000
numbers = [randint(-100, 100) for _ in range(max_size)]

def bubble_sort(array):
    for i in range(len(array) - 1, 0, -1):
        flag = True
        for n in range(i):
            if array[n] < array[n+1]:
                array[n], array[n+1] = array[n+1], array[n]
                flag = False

        if flag == True:
            break
    return array


def bubble_sort_no_smart(array):
    for i in range(len(array) - 1, 0, -1):
        for n in range(i):
            if array[n] < array[n+1]:
                array[n], array[n+1] = array[n+1], array[n]

    return array

time1 = timeit(f'bubble_sort({numbers})',
               setup='from __main__ import bubble_sort',
               number=number_execution)
time2 = timeit(f'bubble_sort_no_smart({numbers})',
               setup='from __main__ import bubble_sort_no_smart',
               number=number_execution)



print(f'Maccив:{numbers}')


print(bubble_sort_no_smart(numbers))
print(bubble_sort(numbers))

time1 = timeit(f'bubble_sort({numbers})',
               setup='from __main__ import bubble_sort',
               number=number_execution)
time2 = timeit(f'bubble_sort_no_smart({numbers})',
               setup='from __main__ import bubble_sort_no_smart',
               number=number_execution)
print(time1)
print(time2)