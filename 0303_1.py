n, m = map(int, input().split())
x = int(input())

for i in range(1, 1501):
    if i % n == 0:
        print(i, abs(x - i))