import random
import array

history = array.array('f')
chance = array.array('f')
sum = 1
balance = 100.0
for i in range(0, 33, 1):
    history.append(0)
    chance.append(100 / 33 - history[i] / sum / 33 * 100)
while 1:
    print(f'Ваш баланс {balance:.2f}')
    print(f'Наиболее вероятное число       {chance.index(max(chance)):.2f}      с вероятностью      {max(chance):.2f}%')

    print('Введите число, которое думаете выпадет')
    print()
    print('-1 для автовыбора')
    print('Введите 33, чтобы выйти')
    try1 = int(input())
    if try1 < 0 or try1 > 32:
        if try1 == 33:
            print('Exit')
            break
        print("Вы ввели недопустимое число. Введите от 0 до 32. 33 для выхода")
    if try1 == -1:
        try1 = int(chance.index(max(chance)))
        print(f'Ваша попытка: {try1}')

    pool = -1
    while pool < 0:
        print('Введите ставку')
        print('(-1 для минимальной. -2    полбанка.     -3       вабанк)')
        pool = float(input())
        if pool == -1:
            pool = 0.1
        elif pool == -2:
            pool = balance / 2
        elif pool == -3:
            pool = balance

    result = int(random.random() * 33)
    print(f'Выпало: {result}')

    if try1 == result:
        print('Вы выиграли')
        balance += pool * 33
    else:
        print('Вы проиграли')
        balance -= pool

    history[result] += 1
    sum += 1
    for i in range(0, 32, 1):
        chance[i] = 100 / 33 - history[i] / sum / 33 * 100
