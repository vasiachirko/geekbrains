list = [7, 5, 3, 3, 2]
a = int(input())
list.append(a)
list.sort(reverse=True)
#list.reverse()
#list.sort(key=lambda val: -1 * val)
print(list)
