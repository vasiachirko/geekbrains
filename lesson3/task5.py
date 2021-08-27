sum = 0
flag = False
while True:
    str = input()
    numbers = str.split(' ')
    for i in numbers:
       try:
           sum += int(i)
       except:
           flag = True
           break

    print(sum)
    if flag:
        break