timeInSeconds = int(input())
hours = timeInSeconds // 3600
minitues = timeInSeconds % 3600 // 60
seconds = timeInSeconds % 60
print(f"{hours:02}:{minitues:02}:{seconds:02}")
