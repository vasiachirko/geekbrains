str = input()
list = str.split(' ')
for tmp in range(0, list.__len__()):
    print(f'{tmp}       {list[tmp][:10]}')

for i, word in enumerate(list, start=1):
    print(f'{i} {word}')