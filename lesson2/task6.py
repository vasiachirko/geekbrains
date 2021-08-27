list1 = []
charects = []
charect = input('Введите название характеристики')
while charect != '':
    charects.append(charect)
    charect = input('Введите название характеристики')


tmp = {}
j = 1
for i in charects:
    examp = input(f'Введите {i}')
    examp = int(examp) if examp.isdigit() else examp
    tmp.update({i: examp})


while tmp[charects[0]] != '':
    cort = (j, tmp)
    list1.append(cort)
    j += 1
    tmp = {}
    for i in charects:
        examp = input(f'Введите {i}')
        tmp.update({i: examp})
list2 = {}
for j in charects:
    list2.update({j: []})
for i in list1:
    print(i)
    for haracter, val in i[1].items():
        list3 = list2[haracter]
        set3 = set(list3)
        set3.add(val)
        list3 = list(set3)
        list2[haracter] = list3
print(list2)






for i, j in list1:
    print(i)
    for haracter, val in j.items():
        list3 = list2[haracter]
        set3 = set(list3)
        set3.add(val)
        list3 = list(set3)
        list2[haracter] = list3
