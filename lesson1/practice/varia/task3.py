digit = int(input())
if digit < 0 or digit > 9:
    print('input is not a digit')
digitStr = str(digit)

string = digitStr + digitStr + digitStr
string2 = digitStr * 3
print (string)
print (string2)

number = digit * 3
print (number)
sum = 0
i = 0
while i < string.__len__():
    sum += int(string[i])
    i += 1
print(sum)