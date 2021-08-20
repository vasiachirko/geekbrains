time = int(input())
seconds = time % 60
time = time - seconds
minutes = time // 60 % 60
time = time - minutes * 60
print(f'{time} {minutes} {seconds}')
