# 6.Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
from itertools import count
from itertools import cycle
lst = []
for p in count(3):
    if p > 10:
        break
    else:
        lst.append(p)
        print(p, end=' ')
print(lst)
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
iter1 = count(10)
i = 0
for p in cycle(iter1):
    if i > 15:
        break
    print(i, p)
    i += 1

# с помощью функции next
iter2 = cycle(count(3))
print(next(iter2))
print(next(iter2))
print(next(iter2))

