"""
Дано четырехзначное число. Верно ли, что цифр в нем расположены по убыванию?
Например, 4311 - нет, 4321 - да, 5542 - нет, 5631 - нет, 9871 - да
"""


numbers = [4311, 4321, 5542, 5631, 9871]
for number in numbers:
    list_figures = list(map(int, list(str(number))))
    sorted_desc = list_figures.copy()
    sorted_desc.sort(reverse=True)
    if list_figures == sorted_desc and len(list_figures) == len(set(list_figures)):
        print(True)
    else:
        print(False)
