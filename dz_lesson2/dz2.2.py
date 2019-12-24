
#2 Для списка реализовать обмен значений соседних элементов,---- НЕ ПОНЯЛ УСЛОВИЕ
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().
my_list1 = input('enter list  :').split()
my_list2 = []  # [1, 3, 5]
my_list3 = []  # [0, 2, 4, 6]
for i in range(len(my_list1)):
    if i % 2 != 0:
        my_list2.append(my_list1[i])
    else:
        my_list3.append(my_list1[i])
my_list4 = list(zip(my_list2, my_list3))
if len(my_list2) > len(my_list3):
    my_list4.append(my_list2[-1])
    print(f'число элементов в исходном списке не четное : {my_list4}')
if len(my_list2) < len(my_list3):
    my_list4.append(my_list3[-1])
    print(f'число элементов в исходном списке  не четное : {my_list4}')
else:
    print(f'число элементов в исходном списке четное : {my_list4}')
