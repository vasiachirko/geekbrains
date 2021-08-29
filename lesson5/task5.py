with open('posled.txt', 'w') as fw:
    string = ''
    for i in range(5, 20):
        string += ' ' + str(i)
    fw.write(string)

with open('posled.txt', 'r') as fr:
    string = fr.read()
    x = string.split()
    a = [int(i) for i in x]
    print(sum(a))
