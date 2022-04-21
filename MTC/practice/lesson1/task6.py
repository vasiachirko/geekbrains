"""
Пользователь вводит четыре числа. Найдите наибольшее четное число среди них. Если оно не существует, выведите фразу "not found"
"""

from random import randrange

numbers = []
evens = []
for i in range(4):
    numbers.append(randrange(10))#input('Введите число: '))
print(numbers)
for i in numbers:
    if i % 2 == 0:
        evens.append(i)
try:
    print(max(evens))
except ValueError:
    print('not found')
