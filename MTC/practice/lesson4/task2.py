"""
Дана квадратная матрица. Вычислить сумму элементов главной или побочной диагонали в зависимости от выбора пользователя.
Сумма элементов любой диагонали должна вычисляться в одной и той же функции.
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
    print(my_list_in_lists)


def sum_diag(matrix, diagonal_type):
    if diagonal_type == 'гл':
        print(sum(element[index] for index, element in enumerate(matrix)))
    elif diagonal_type == 'поб':
        print(sum(element[len(matrix)-1-index] for index, element in enumerate(matrix)))


sum_diag(lists, 'поб')
