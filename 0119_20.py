n, x = map(int, input().split())
l = list(map(int, input().split()))

for i in range(len(l)):
    if x == l[i]:
        print(i + 1)
        break