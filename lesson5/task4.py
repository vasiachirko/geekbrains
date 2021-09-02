translate = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', "Four": 'Четыре'}
strs = []
with open('numbers.txt', 'r', encoding='utf8') as fo:
    while s:=fo.readline():
        str =s.split()
        str_joined1 = ' '.join(str[1:])
        strs2 = [translate[str[0]], str_joined1]
        str_res = ' '.join(strs2)
        strs.append(str_res+'\n')

        str2 = s.replace(str[0], translate[str[0]])
with open('translated.txt', 'w') as fw:
    fw.writelines(strs)