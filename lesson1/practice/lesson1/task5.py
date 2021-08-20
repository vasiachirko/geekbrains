earnings = int(input("Введите прибыль"))
cost = int(input("Введите издержки"))

if earnings > cost:
    print("Прибыль")
    profit = earnings - cost
    print(f"Рентабельность прибыли {profit/earnings}")

    numPeople = int(input("Ввведите количество человек"))
    print(f"Прибыль фирмы в расчёте на одного сотрудника {profit/numPeople}")
else:
    print("Убыток")
