"""
Дано четырехзначное число. Определите, есть ли одинаковые цифры в нем.
"""

number = 1234
number2 = 1123


def unique_digit(number):
    list_figures = list(map(int, list(str(number))))
    if not len(set(list_figures)) == len(list_figures):
        print(True)
    else:
        print(False)


unique_digit(number)
unique_digit(number2)