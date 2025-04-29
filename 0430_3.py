n, m = map(int, input().split())

x = 1
y = n
total = 0
for i in range(m):
    y = x * y
    total += y
    x = y




print(total)
