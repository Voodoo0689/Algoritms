import random
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_index = 0
max_index = 0
step = 1
sum = 0

for i in array:
    if array[min_index] > i:
        min_index = array.index(i)
    elif array[max_index] < i:
        max_index = array.index(i)

if max_index - min_index < 0:
    step = -1

for i in array[min_index + step:max_index:step]:
    sum += i

print(
    f'Сумма элементов между минимальным ({array[min_index]})',
    f' и максимальным ({array[max_index]}) элементами: {sum}'
    )
