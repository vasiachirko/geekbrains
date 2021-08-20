num = int(input())
max = 0
while num != 0:
    cif = num % 10
    if cif > max:
        max = cif
    num //= 10
print(max)