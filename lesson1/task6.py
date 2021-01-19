distanceStart = int(input("Сколько км спортсмен пробежал в первый день"))
distanceTotal = int(input("Сколько км в день должен пробегать спортсмен"))
day = 1
distance = distanceStart
while distance < distanceTotal:
    distance *= 1.1
    day += 1
print(f"Спортсмен пробежал не менее {distanceTotal} км на {day} день")