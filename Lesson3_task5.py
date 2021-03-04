import random

SIZE = 10
MIN_ITEM = -99
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

neg_max = -100

for i in array:
    if 0 > i > neg_max:
        neg_max = i
print(
    f"В массиве максимальный отрицательный элемент: {neg_max}.",
    f'Находится в массиве на позиции {array.index(neg_max)}'
    )





