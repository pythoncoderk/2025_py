n, m = map(int, input().split())
l = [int(input()) for i in range(m)]

for i in l:
    x = (i / n) + 0.5
    y = int(x) * n
    print(n if y == 0 else y)