from random import randint

n = 10
len_size = 2 * n + 1
numbers = [randint(1, 100) for _ in range(len_size)]


def gnome(data):
    i, j, size = 1, 2, len(data)
    while i < size:
        if data[i - 1] <= data[i]:
            i, j = j, j + 1
        else:
            data[i - 1], data[i] = data[i], data[i - 1]
            i -= 1
            if i == 0:
                i, j = j, j + 1
    return data


def medium(items):
    i = len(items) // 2 + 1
    return items[i]


print(numbers)
print(gnome(numbers))
print(medium(gnome(numbers)))
