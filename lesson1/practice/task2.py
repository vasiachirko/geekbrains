def remnant(time):
    return time % 60

def division(time):
    return time // 60

time = int(input())
seconds = remnant(time)
time = division(time)
minitues = remnant(time)
time = division(time)
hours = remnant(time)
print(f'{hours:2.0f}:{minitues:2.0f}:{seconds:2.0f}')
print(f'{hours//10}{hours%10}:'
      f'{minitues//10}{minitues%10}:'
      f'{seconds//10}{seconds%10}')