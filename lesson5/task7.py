import json

dictionary = {}
prib = []
with open('nalog.txt', 'r') as fr:
    while s := fr.readline():
        strings = s.split()
        naim, form, viruch, izd = strings
        dictionary[naim] = int(viruch) - int(izd)
        prib.append(dictionary[naim])

summa = 0
count = 0
for i in prib:
    if i > 0:
        summa += i
        count += 1
res = [dictionary, {'average_profit' : summa/count}]
with open('json_res.txt', 'w') as fw:
    fw.write(json.dumps(res))