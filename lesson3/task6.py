def int_func2(text):
    text2 = text[0]
    TEXT2 = text2.upper()
    return TEXT2 + text[1:]

def int_func(text):
    return text.capitalize()

def int2_func2(text):
    return text.capitalize()

def int2_func2(text):
    text2 = text.split(' ')
    s = int_func(text2[0])
    s2 = int_func2(text2[0])

    for j in range(1, text2.__len__()):
        i = text2[j]

        str = int_func(i)
        str2 = int_func2(i)

        str_list = [s, str]
        s = ' '.join(str_list)
        s2 = s2 + ' ' + str
    return s

print(int2_func2('text2 ospdfa'))