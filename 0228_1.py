n, m = map(int, input().split())
a, b = map(int, input().split())

l = [int(input()) for i in range(m)]

for i in l:
    x = abs(a - i)
    y = abs(b - i)
    if x < y:
        print(a)
    else:
        print(b)