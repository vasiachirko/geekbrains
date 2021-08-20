def fib(param):
    if param == 0:
        return 0
    elif param == 1:
        return 1
    else:
        return fib(param-1)+fib(param-2)

print(fib(6))