"""
Сгенерировать десять массивов из случайных чисел. Вывести их и сумму их элементов на экран.
Найти среди них один с максимальной суммой элементов. Указать какой он по счету, повторно вывести этот массив и сумму его элементов.
Заполнение массива оформить в виде отдельной функции.
"""

from random import randrange


def init_list():
    my_list = []
    for index_of_element in range(10):
        my_list.append(randrange(10))
    return my_list


lists = []
for index_of_list in range(10):
    lists.append(init_list())
for my_list_in_lists in lists:
    print(my_list_in_lists, sum(my_list_in_lists))

sums = [(sum(my_list_in_lists), my_list_in_lists) for my_list_in_lists in lists]
index_and_sum_with_list = [(index_of_sum, sum_and_list) for index_of_sum, sum_and_list in enumerate(sums, start=1)]
max_index_and_sum_with_list = max(index_and_sum_with_list, key=lambda i: i[1][0])
print(max_index_and_sum_with_list[0])
print(max_index_and_sum_with_list[1][0])
print(max_index_and_sum_with_list[1][1])
