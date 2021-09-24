"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class DevZero(Exception):
    pass


def division(a, b):
    if b == 0:
        raise DevZero('На ноль делить нельзя')
    else:
        return a / b


a = int(input())
b = int(input())
try:
    result = division(a, b)
except DevZero:
    print(DevZero)
else:
    print(result)
