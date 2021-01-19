print("Введите прибыль")
earnings = int(input())
print("Введите издржки")
cost = int(input())

if earnings > cost:
    print("Прибыль")
    profit = earnings - cost
    print(f"Рентабельность прибыли {profit/earnings}")

    print("Ввведите количество человек")
    numPeople = int(input())
    print(f"Прибыль фирмы в расчёте на одного сотрудника {profit/numPeople}")
else:
    print("Убыток")
