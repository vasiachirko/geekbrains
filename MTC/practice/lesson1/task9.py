"""
Дано трехзначное число. Переставьте первую и последнюю цифры
"""

number = 852
last_digit = number % 10
first_digit = number // 100
last_digit, first_digit = first_digit, last_digit
print(first_digit * 100 +
      number % 100 // 10 * 10 +
      last_digit)