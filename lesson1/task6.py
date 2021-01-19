print("Сколько км спортсмен пробежал в первый день")
distanceStart = int(input())
print("Сколько км в день должен пробегать спортсмен")
distanceTotal = int(input())
day = 1
distance = distanceStart
while distance < distanceTotal:
    distance *= 1.1
    day += 1
print(f"Спортсмен пробежал не менее {distanceTotal} км на {day} день")