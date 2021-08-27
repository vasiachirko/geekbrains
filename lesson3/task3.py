def sum2(param1, param2, param3):
    if param1 < param2:
        if param3 < param1:
            return param1 + param2
        else:
            return param2 + param3
    else:
        if param3 < param2:
            return param1 + param2
        else:
            return param3 + param1

def sum2_2(a, b, c):
    list = [a, b, c]
    list.sort(reverse=True)
    return sum(list[:2])

a = int(input())
b = int(input())
c = int(input())
result = sum2_2(a, b, c)
print(result)
