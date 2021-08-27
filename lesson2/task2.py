list = []
a = input()
while a!='':
    list.append(a)
    a = input()
print(list)
list1 = list.copy()
for i in range(0, list.__len__()):
    if (i % 2 == 0) and (i != list.__len__()-1):
        c = list[i]
        list[i] = list[i+1]
        list[i+1] = c
print(list)
list1[:list1.__len__()//2*2:2], list1[1:list1.__len__()//2*2:2] = list1[1:list1.__len__()//2*2:2], list1[:list1.__len__()//2*2:2]
print(list1)