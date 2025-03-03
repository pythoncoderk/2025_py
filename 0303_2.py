n, m = map(int, input().split())
l = [int(input()) for i in range(m)]

for i in l:
    if i <= n:
        print(n)
    else:
        x = i / n
        x += 0.5
        print(int(x) * n)
