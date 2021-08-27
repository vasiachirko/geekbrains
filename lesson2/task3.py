def get_month():
    pass
#проверка правильности ввода месяца

list = [[1, 2, 12], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
seasons = ['winter', 'spring', 'sumer', 'autumn']
dict = {'winter': [1, 2, 12], 'spring': [3, 4, 5], 'summer': [6, 7, 8], 'autumn': [9, 10, 11]}
a = int(input())
for val in range(0, list.__len__()):
    if a in list[val]:
        if val == 0:
            print('winter')
        elif val == 1:
            print('spring')
        elif val == 2:
            print('summer')
        elif val == 3:
            print('autumn')
        else:
            print('No such month')

print(seasons[a % 12 // 3])
for season, month in dict.items():
    if a in month:
        print(season)