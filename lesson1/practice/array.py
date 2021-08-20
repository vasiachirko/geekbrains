import array

def f(param):
    fib = array.array('I')
    res = array.array('I')
    fib.append(0)
    fib.append(1)
    res.append(fib[0])
    i = 2
    j = 1
    while j < param:
        fib.append(fib[i-2]+fib[i-1])
        if fib[i] % 2 == 0:
            j += 1
            res.append(fib[i])
        i += 1
    return res

print(f(3))