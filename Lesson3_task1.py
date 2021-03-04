result = {}
for n in range(2, 10):
    result[n] = []
    for f in range(2, 100):
        if f % n == 0:
            result[n].append(f)
    print(
        f'Для числа {n} кратны - {len(result[n])}. Кратные числа: {result[n]}.'
        )
