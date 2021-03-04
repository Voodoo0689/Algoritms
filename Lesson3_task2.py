import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

index_even = []

for n in array:
    if n % 2 == 0:
        index_even.append(array.index(n))

print(f'Индексы чётных элементов первого массива: {index_even}')
