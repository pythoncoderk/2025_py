n, m = map(int, input().split())

for i in range(n):
    x = int(input())
    x = (x / n) + 0.5
    x = int(x)
    if x == 0:
        print(n)
    else:
        print(n * x)

