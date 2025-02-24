n = int(input())

x = n / 1000

if 0.1 > x: print("00")
elif 0.1 <= x <= 5: print(str(int(x * 10)).zfill(2))
elif 6 <= x <= 30: print(int(x + 50))
elif 35 <= x <= 70: print(int(((x - 30) // 5) + 80))
else: print("89")