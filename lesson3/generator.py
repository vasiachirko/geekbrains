def fun():
    for i in range(10):
        yield i
    for i in range(20, 30):
        yield i

g = (x for x in fun())

for i in g:
    print(i)