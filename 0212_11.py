n = int(input())
x = 0
if 1 <= n <= 99:
    x = 1
elif 100 <= n <= 199:
    x = 2
elif 200 <= n <= 299:
    x = 3
elif 300 <= n <= 399:
    x = 4

if x == 1:
    print(100 - n)
if x == 2:
    print(200 - n)
if x == 3:
    print(300 - n)