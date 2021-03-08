import timeit
import cProfile

numbers = "0123456789"


def rev(x):
    text = ''.join(reversed(x))
    return text


#print(timeit.timeit('rev(numbers*10)', number=1000, globals=globals()))         #0.002940100000000001
#print(timeit.timeit('rev(numbers*100)', number=1000, globals=globals()))        #0.020791
#print(timeit.timeit('rev(numbers*1000)', number=1000, globals=globals()))       #0.2045256
#print(timeit.timeit('rev(numbers*10000)', number=1000, globals=globals()))      #2.1058719000000004
#print(timeit.timeit('rev(numbers*100000)', number=1000, globals=globals()))     #20.104114099999997
#cProfile.run('rev(numbers*100000)')
"""
        5 function calls in 0.022 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001    0.022    0.022 <string>:1(<module>)
        1    0.000    0.000    0.021    0.021 lesson2_task3.py:7(rev)
        1    0.000    0.000    0.022    0.022 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.021    0.021    0.021    0.021 {method 'join' of 'str' objects}
"""
# Сложность: O(n) линейная сложность. Время возрастает линейно и прямо пропорционально количеству передаваемых данных.


def cycle(x):
    y = ""
    for i in x:
        y = i + y
    return y


#print(timeit.timeit('cycle(numbers*100)', number=1000, globals=globals()))         #0.1296545
#print(timeit.timeit('cycle(numbers*200)', number=1000, globals=globals()))         #0.33759249999999996
#print(timeit.timeit('cycle(numbers*400)', number=1000, globals=globals()))         #0.8923346
#print(timeit.timeit('cycle(numbers*800)', number=1000, globals=globals()))         #2.2229356000000005
#print(timeit.timeit('cycle(numbers*1600)', number=1000, globals=globals()))        #6.482493400000001
#cProfile.run('cycle(numbers*10000)')
"""
4 function calls in 0.406 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.406    0.406 <string>:1(<module>)
        1    0.406    0.406    0.406    0.406 lesson2_task3.py:31(cycle)
        1    0.000    0.000    0.406    0.406 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""
# Сложность: O(n^2) квадратичная сложность.
# Я сомневаюсь в сложности, по идее это обычный цикл О(n), но с условием внутри.
# И явно видно, что при увеличении нагрузки в два раза
# время работы увеличивается почти в три. Поправьте, пожалуйста если я не прав.


def cut(x):
    x = x[::-1]
    return x


#print(timeit.timeit('cut(numbers*100)', number=1000, globals=globals()))        #0.0017436000000000014
#print(timeit.timeit('cut(numbers*200)', number=1000, globals=globals()))        #0.0028571000000000013
#print(timeit.timeit('cut(numbers*400)', number=1000, globals=globals()))        #0.004981599999999999
#print(timeit.timeit('cut(numbers*800)', number=1000, globals=globals()))        #0.009159599999999997
#print(timeit.timeit('cut(numbers*1600)', number=1000, globals=globals()))       #0.0165577
#cProfile.run('cut(numbers*1000000)')
"""
4 function calls in 0.013 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.003    0.003    0.013    0.013 <string>:1(<module>)
        1    0.010    0.010    0.010    0.010 lesson2_task3.py:56(cut)
        1    0.000    0.000    0.013    0.013 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""
# Сложность: O(n) линейная сложность.
# Время возрастает линейно и прямо пропорционально количеству передаваемых данных.

def rec(x):
    x = list(x)
    if len(x) == 1:
        return x
    return x[-1] + "".join(rec(x[:-1]))


#print(timeit.timeit('rec(numbers*5)', number=100, globals=globals()))          #0.0051573999999999925
#print(timeit.timeit('rec(numbers*10)', number=100, globals=globals()))         #0.017568299999999995
#print(timeit.timeit('rec(numbers*20)', number=100, globals=globals()))         #0.06673000000000001
#print(timeit.timeit('rec(numbers*40)', number=100, globals=globals()))         #0.2709792
#print(timeit.timeit('rec(numbers*80)', number=100, globals=globals()))         #1.0248431999999998
#cProfile.run('rec(numbers*99)')
"""
2972 function calls (1983 primitive calls) in 0.025 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.025    0.025 <string>:1(<module>)
    990/1    0.016    0.000    0.025    0.025 lesson2_task3.py:79(rec)
        1    0.000    0.000    0.025    0.025 {built-in method builtins.exec}
      990    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
      989    0.008    0.000    0.008    0.000 {method 'join' of 'str' objects}
"""
# Сложность O(2^n) экспоненциальная. Время работы такого алгоритма удваивается с
# каждым очередным дополнением к набору данных
