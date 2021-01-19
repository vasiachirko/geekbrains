timeInSeconds = int(input())
hours = timeInSeconds // 3600;
minitues = timeInSeconds % 3600 // 60;
seconds = timeInSeconds % 60;
print(f"{hours}:{minitues}:{seconds}")
