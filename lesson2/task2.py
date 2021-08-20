list = []
a = input()
while a!='':
    list.append(a)
    a = input()
print(list)
for i in range(0, list.__len__()):
    if (i % 2 == 0) and (i != list.__len__()-1):
        c = list[i]
        list[i] = list[i+1]
        list[i+1] = c
print(list)