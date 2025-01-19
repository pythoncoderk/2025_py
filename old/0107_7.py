n = int(input())

x = n // 60
y = n % 60

h = str(21 + x).zfill(2)
print(h + ":" + str(y).zfill(2))

