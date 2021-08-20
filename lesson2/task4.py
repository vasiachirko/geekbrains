str = input()
list = str.split(' ')
for tmp in range(0, list.__len__()):
    print(f'{tmp}       {list[tmp][:10]}')