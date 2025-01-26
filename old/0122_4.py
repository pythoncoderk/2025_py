n = int(input())

l = list(map(int, input().split()))

for i in range(n):
    if l[i] % 2 == 0:
        if i == n - 1:
            print(l[i])
        else:
            print(l[i], end=" ")