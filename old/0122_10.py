n, a, b = map(int, input().split())

l = list(map(int, input().split()))

for i in range(n):
    if l[i] == a + b:
        print(i + 1)
