"""
Дано четырехзначное число. Если оно читается слева направо и справа налево одинаково, то вывести yes, иначе no.
"""
from time import time


def check_palindrome(string):
    # transversing the string from last to first
    reversed_string = string[::-1]
    if string == reversed_string:
        print(string, "is a palindrome")
    else:
        print(string, "is not a Palindrome")


def check_palindrome2(string):
    l = len(string)
    first = 0
    last = l - 1
    is_palindrome = True

    # ensuring that we do not iterate through more than half                          #   of the list
    while first < last:
        # if the first character is same as last character keep     #       moving further
        if string[first] == string[last]:
            first = first + 1
            last = last - 1
        # if the characters at first and last do not match break #      the loop
        else:
            is_palindrome = False
            print(string, "is not a Palindrome")
            break
    print(string, "is a palindrome")


time_start = time()
for i in range(100):
    check_palindrome("RADAR")
    check_palindrome("PythonPool")
time_end = time()
print(time_start - time_end)

#0.01
#0.02
