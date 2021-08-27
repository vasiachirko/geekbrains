def func(a,b):
    try:
        return a/b
    except:
        print('Деление на 0')

def func2(a,b):
    if b != 0:
        return a/b
    else:
        print('Деление на 0')


c = func(5, 0)
print(f'{c:.2f}')