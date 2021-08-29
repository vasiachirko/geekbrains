with open('lessons.txt', 'r', encoding='utf8') as fr:
    text = fr.readlines()
dict = {}
for i in text:
    predmet = i.split(':', 1)[0]
    num = 0
    summa = 0
    for dig in i:
        if dig.isdigit():
            num *= 10
            num += int(dig)
        else:
            summa += num
            num = 0
    dict[predmet] = summa
print(dict)
