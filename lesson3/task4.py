def my_func(x, y):
    print(f'{x**y:.5f}')
    result = 1
    for i in range(0, abs(y)):
        result /= x
    print(f'{result:.5f}')

x = int(input())
y = int(input())
my_func(x,y)